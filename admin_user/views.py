from django.shortcuts import render, get_object_or_404, redirect
from client_user.models import *
from agent_user.models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from authentication.decorators import *
from django.contrib.auth.models import User
from django.contrib import messages


from .forms import FineForm
 

# Create your views here.


# Create your views here.


                    #<---------------------ADMIN SECTION STARTS------------------->
@login_required(login_url='/')  
@admin_only          
   
def admin_homepage(request):
    clients = Client.objects.all()
    agents = Agent.objects.all()
    fines = Fine.objects.all()
    pending = fines.filter(Q(status='Failed') | Q(status='Pending')).count()
    total_fines = fines.count()
    total_clients = clients.count()
    total_agents = agents.count()
    context = {'clients': clients,'pending': pending,'agents': agents,'fines': fines, 'total_clients': total_clients,'total_fines': total_fines, 'total_agents': total_agents }
    return render(request, 'main_pages/admin_dashboard.html', context)



                  #<---------------------ADMIN SECTION ENDS------------------->

                  #<---------------------CLIENT SECTION STARTS------------------->
@login_required(login_url='/') 
                      
def clients(request):
    clients = Client.objects.all()
    total_clients = clients.count()
    context = {'clients': clients, 'total_clients': total_clients }
    return render(request, 'main_pages/sub_pages/client/clientview.html', context)
@login_required(login_url='/')
@admin_only        
def addclients(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Check if all fields are filled
        if not all([name, address, contact, email, username, password, latitude, longitude]):
            messages.error(request, 'Please fill in all fields.')
            return redirect('addclients')

        user = User.objects.create_user(username=username, password=password, email=email)

        # Create a new Client instance and save it to the database
        new_client = Client(user=user, name=name, address=address, contact=contact, username=username, latitude=latitude, longitude=longitude)
        new_client.save()
        return redirect('/clients')

    return render(request, 'main_pages/sub_pages/client/addclients.html')
@login_required(login_url='/')
@admin_only        
def editclients(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    context = {'client': client}
    return render(request, 'main_pages/sub_pages/client/editclient.html', context)
@login_required(login_url='/')
@admin_only        
def updateclient(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.address = request.POST.get('address')
        client.contact = request.POST.get('contact')
        # client.email = request.POST.get('email')
        # client.username = request.POST.get('username')
        # client.password = request.POST.get('password')
        client.save()

        return redirect('clients')  
    context = {'client': client}
    return render(request, 'main_pages/sub_pages/client/editclient.html', context)
@login_required(login_url='/')
@admin_only        
def deleteclient(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    
    if request.method == 'POST':
        client.delete()
        return redirect('/clients')

    context = {'client': client}
    return render(request, 'main_pages/sub_pages/client/clientview.html', context)

                   #<---------------------CLIENT SECTION ENDS------------------->

                   #<---------------------AGENT SECTION STARTS------------------->
@login_required(login_url='/')
@admin_only        
def agents(request):
    agents = Agent.objects.all()
    context = {'agents': agents, }
    return render(request, 'main_pages/sub_pages/agents/agentview.html', context)
@login_required(login_url='/')
@admin_only        
def editagent(request, agent_id):
    agent = Agent.objects.get(pk = agent_id)
    context = {'agent': agent }
    return render(request, 'main_pages/sub_pages/agents/editagent.html', context)
@login_required(login_url='/')
@admin_only        
def updateagent(request, agent_id):
    agent = get_object_or_404(Agent, pk=agent_id)

    if request.method == 'POST':
        agent.name = request.POST.get('name')
        agent.address = request.POST.get('address')
        agent.contact = request.POST.get('contact')
        agent.area = request.POST.get('area')
        agent.register_id = request.POST.get('register_id')
        # agent.email = request.POST.get('email')
        # agent.password = request.POST.get('password')
        agent.username = request.POST.get('username')

        # Check if a new licenses file is provided
        licenses_file = request.FILES.get('licenses')
        if licenses_file:
            agent.licenses = licenses_file

        # Check if a new agent image file is provided
        agent_img_file = request.FILES.get('agent_img')
        if agent_img_file:
            agent.agent_img = agent_img_file

        # Check if a new vehicle image file is provided
        vehicle_img_file = request.FILES.get('vehicle_img')
        if vehicle_img_file:
            agent.vehicle_img = vehicle_img_file

        agent.save()
        return redirect('/agents')

    context = {'agent': agent}
    return render(request, 'main_pages/sub_pages/agents/editagents.html', context)
@login_required(login_url='/')
@admin_only        
def deleteagent(request, agent_id):
    agent = get_object_or_404(Agent, pk=agent_id)
    if request.method == 'POST':
        agent.delete()
        return redirect('/agents')

    context = {'agent':agent}
    return render(request, 'main_pages/sub_pages/agents/agentview.html', context)
@login_required(login_url='/')
@admin_only        
def addagents(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        area = request.POST.get('area')
        register_id = request.POST.get('register_id')
        licenses = request.FILES.get('licenses')
        agent_img = request.FILES.get('agent_img')
        vehicle_img = request.FILES.get('vehicle_img')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Basic form validation
        if not all([name, address, contact, area, register_id, licenses, agent_img, vehicle_img, email, password, username, latitude, longitude]):
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'main_pages/sub_pages/agents/addagents.html')

        user = User.objects.create_user(username=username, password=password, email=email)
        new_agent = Agent(
            user=user,
            name=name,
            address=address,
            contact=contact, 
            vehicle_img=vehicle_img,
            agent_img=agent_img,
            licenses=licenses,
            register_id=register_id,
            area=area,
            username=username,
            latitude=latitude,
            longitude=longitude
            
        )
        new_agent.save()
        return redirect('/agents')

    return render(request, 'main_pages/sub_pages/agents/addagents.html')

                  #<---------------------AGENT SECTION ENDS------------------->


                  #<---------------------FINES SECTION STARTS------------------->
@login_required(login_url='/')
def fines(request):
    fines = Fine.objects.all()
    context = {'fines': fines } 
    return render(request, 'main_pages/sub_pages/Fines/fineview.html', context)


@login_required(login_url='/')
def editfine(request, client_id):
    finelist = get_object_or_404(Fine, pk=client_id)
    context = {'finelist': finelist }
    return render(request, 'main_pages/sub_pages/Fines/editfine.html', context)
@login_required(login_url='/')
def deletefine(request, fine_id):
    fine = get_object_or_404(Fine, pk=fine_id)
    
    if request.method == 'POST':
        fine.delete()
        return redirect('/fines')

    context = {'fine': fine}
    return render(request, 'main_pages/sub_pages/client/clientview.html', context)
@login_required(login_url='/')
def updatefine(request, fine_id):
    fine = get_object_or_404(Fine, pk=fine_id)

    if request.method == 'POST':
        fined_amount = request.POST.get('fined_amount')
        fine.fined_amount = fined_amount
        fine.save()

        return redirect('fines')

    context = {'finelist': fine}
    return render(request, 'main_pages/sub_pages/Fines/editfine.html', context)
@login_required(login_url='/')
def addfine(request):
    clients = Client.objects.all()
    agents = Agent.objects.all()

    if request.method == 'POST':
        form = FineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fines')
    else:
        form = FineForm()

    context = {'clients': clients, 'agents': agents, 'form': form}
    return render(request, 'main_pages/sub_pages/Fines/addfines.html', context)
@login_required(login_url='/')
def recvfines(request):
    paid_fines = Fine.objects.filter(status='Paid')
    print(paid_fines)
    return render(request, 'main_pages/sub_pages/Fines/recivedfines.html', {'paid_fines': paid_fines})

@login_required(login_url='/')
def notify(request):
    clients = Client.objects.all()
    context = {'clients': clients}

    if request.method=="POST":

        client = Client.objects.get(pk=request.POST.get('client')) 
        notification_type = 'admin'
        notification_text = request.POST.get('notification_text')
        # print(client)
        Notification.objects.create(client=client,notification_type=notification_type,notification_text=notification_text)
    return render(request, 'main_pages/sub_pages/agents/notify.html', context )

                    #<---------------------FINES SECTION ENDS------------------->


@login_required(login_url='/')
def viewAgentsLocation(request): 
    
    agents = AgentCurrentLocation.objects.all()  
    print(agents)
    context = {'agents': agents} 
    return render(request,'main_pages/agentlocationview.html',context)