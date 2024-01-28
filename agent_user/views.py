from django.http import JsonResponse
from django.shortcuts import render,redirect
from client_user.models import *
from agent_user.models import *
from django.db.models import Q
from django.db import models, connection
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from authentication.decorators import *

@login_required(login_url='/')
def agent_homepage(request):
    clients = Client.objects.all()
    agents = Agent.objects.all()
    fines = Fine.objects.all()
    pending = fines.filter(Q(status='Failed') | Q(status='Pending')).count()
    context = {'clients': clients,'pending': pending,'agents': agents,'fines': fines }
    return render(request, 'main_pages/agent_dashboard.html', context)
@login_required(login_url='/')

def spots(request):
    clients = Client.objects.all() 
    total_clients = clients.count()  
    agent_latitude = request.user.agent.latitude
    agent_longitude = request.user.agent.longitude
 
    raw_query = f'''
    SELECT *,
           (6371 * acos(
               cos(radians({agent_latitude})) * cos(radians(latitude)) * cos(radians(longitude) - radians({agent_longitude}))
               + sin(radians({agent_latitude})) * sin(radians(latitude))
           )) AS distance
    FROM "{Client._meta.db_table}"
    WHERE (6371 * acos(
               cos(radians({agent_latitude})) * cos(radians(latitude)) * cos(radians(longitude) - radians({agent_longitude}))
               + sin(radians({agent_latitude})) * sin(radians(latitude))
           )) <= 100
'''

# Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        columns = [col[0] for col in cursor.description]
        nearby_clients_data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # Extract primary key values from the raw query results
    nearby_client_pks = [client_data['id'] for client_data in nearby_clients_data]

    # Filter the Client queryset using the extracted primary keys
    today = timezone.now().date()

    print(today)

    nearby_clients = Client.objects.filter(pk__in=nearby_client_pks)
    result_clients = Client.objects.filter(
    pk__in=nearby_client_pks
    ).exclude(
        completed__date_created__date=today
    ).exclude(
        fine__status='Pending'
    ).exclude(
        fine__status='Failed'
    ).distinct()
     
    agent = Agent.objects.get(user=request.user)
    context = {'clients': result_clients, 'total_clients': total_clients , 'agent': agent} 
    return render(request,'main_pages/sub_pages/agents/spots.html',context)
@login_required(login_url='/')

def sendalert(request,clientid):
    client = Client.objects.get(pk=clientid)
    agent = Agent.objects.get(pk=request.user.agent.id)
    notification_type = 'agent'
    notification_text = 'I Will be arriving Soon'
    # print(client)
    Notification.objects.create(client=client,agent=agent,notification_type=notification_type,notification_text=notification_text)
    return redirect('/spots')
@login_required(login_url='/')

def completed(request,clientid):
    client = Client.objects.get(pk=clientid)
    agent = Agent.objects.get(pk=request.user.agent.id)
    notification_type = 'agent'
    notification_text = 'The waste has been collected from your house'
    # print(client)
    Notification.objects.create(client=client,agent=agent,notification_type=notification_type,notification_text=notification_text)


    Completed.objects.create(client=client,agent=agent)
    return redirect('/spots')
    # user = User.objects.create_user(username=username, password=password, email=email)
@login_required(login_url='/')

def agentReport(request):

    reports = Completed.objects.filter(agent=request.user.agent)

    print(reports)

    return render(request,'main_pages/sub_pages/agents/reports.html',{'reports':reports})


@login_required(login_url='/')

def update_agent_location(request):
    if request.method == 'POST':
        agent_id = request.user.agent.id    
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        agent_location, created = AgentCurrentLocation.objects.get_or_create(agent_id=agent_id)

        # Update the agent's location
        agent_location.latitude = latitude
        agent_location.longitude = longitude
        agent_location.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@login_required(login_url='/')

def viewFines(request):
    fines = Fine.objects.filter(agent=request.user.agent)
    print(fines)