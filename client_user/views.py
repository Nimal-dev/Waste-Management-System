from django.shortcuts import render,get_object_or_404
from . models import *
from authentication.decorators import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.db import  connection
# Create your views here.
from django.utils import timezone
 
from django.http import JsonResponse
from django.conf import settings
import razorpay
import json
from django.contrib.auth.decorators import user_passes_test

razrclient = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required(login_url='/')
def client_homepage(request):
    clients = Client.objects.all()
    agents = Agent.objects.all()
    fines = Fine.objects.all()
    total_fines = fines.count()
    total_clients = clients.count()
    total_agents = agents.count()
    context = {'clients': clients,'agents': agents,'fines': fines, 'total_clients': total_clients,'total_fines': total_fines, 'total_agents': total_agents }
    return render(request, 'main_pages/client_dashboard.html', context)
@login_required(login_url='/')
def myprofile(request):
    client = Client.objects.all()
    context = {'client': client}
    return render(request, 'main_pages/sub_pages/client/clientprofile.html', context )
@login_required(login_url='/')
def viewAgentClient(request): 
    client_latitude = request.user.client.latitude
    client_longitude = request.user.client.longitude
 
    raw_query = f'''
    SELECT *,
           (6371 * acos(
               cos(radians({client_latitude})) * cos(radians(latitude)) * cos(radians(longitude) - radians({client_longitude}))
               + sin(radians({client_latitude})) * sin(radians(latitude))
           )) AS distance
    FROM "{AgentCurrentLocation._meta.db_table}"
    WHERE (6371 * acos(
               cos(radians({client_latitude})) * cos(radians(latitude)) * cos(radians(longitude) - radians({client_longitude}))
               + sin(radians({client_latitude})) * sin(radians(latitude))
           )) <= 100
'''

# Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        columns = [col[0] for col in cursor.description]
        nearby_agents_data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    # Extract primary key values from the raw query results
    nearby_agent_pks = [client_data['id'] for client_data in nearby_agents_data]

    # Filter the Client queryset using the extracted primary keys
    today = timezone.now().date()
 
 
    result_agents = AgentCurrentLocation.objects.filter(
    pk__in=nearby_agent_pks
    )
      
    context = {'clients': result_agents} 
    return render(request,'main_pages/sub_pages/client/agentview.html',context)
@login_required(login_url='/')
def viewFinesClient(request):
    fines = Fine.objects.filter(client=request.user.client.id)
    context = {'fines': fines } 
    return render(request, 'main_pages/sub_pages/Fines/userviewfine.html', context)


client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
@login_required(login_url='/')
def create_razorpay_order(request, fine_id):
    try:
        # Fetch the fine details from the database based on fine_id
        fine = Fine.objects.get(id=fine_id)
        
        # Amount should be in paise
        amount = int(fine.fined_amount * 100)
        
        order = razrclient.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1',
        })
         
      

        return JsonResponse({'order_id': order['id'], 'amount': order['amount']})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@login_required(login_url='/')
def razorpay_payment_callback(request,fineid):
        
        fine = Fine.objects.get(id=fineid)
        
        fine.status='Paid'
        fine.save()

        # Here, you can update your fine status to 'Paid' in the database
        # Update the 'status' field of your fine model to 'Paid'

        return redirect('/viewfinesclient')