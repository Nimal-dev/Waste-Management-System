from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from client_user.models import *
from agent_user.models import *
from admin_user.models import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
# from django.contrib.auth.decorators import login_required
from .decorators import *
# from django import forms



# Create your views here.
@unauthenticated_user
def loginpage(request):  
    # admin_user = Admin.objects.all()                   
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)


                if(request.user.is_superuser==1):
                    return redirect('admin_homepage') 
                      

                if hasattr(request.user, 'client'):
                     return redirect('client_homepage')
                elif hasattr(request.user,'agent'):
                     return redirect('agent_homepage')
                     
                     

                # if(usertype=='client'):
                # elif(usertype=='agent'):
                #      return redirect('agent_homepage')
                     
            else:
                messages.error(request, 'Username or Password is incorrect!')
                return redirect('/')  

        return render(request, 'auth_pages/login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')

@unauthenticated_user
def registerpage(request):                                 #REGISTER PAGE

        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                latitude = request.POST.get('latitude')
                longitude = request.POST.get('longitude')
                # user_type = request.POST.get('usertype')

                print('latitude', latitude)
                print('longitude', longitude)
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)
                return redirect('/')
        context= {'form': form}
        return render(request, 'auth_pages/registration.html', context)