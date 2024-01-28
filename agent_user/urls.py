from django.urls import path
from . import views

urlpatterns = [
    path('agent_home/', views.agent_homepage, name='agent_homepage'),
    path('spots/', views.spots, name='spots'),
    path('sendalert/<int:clientid>', views.sendalert, name='sendalert'),
    path('completed/<int:clientid>', views.completed, name='completed'),
    path('agentreports/', views.agentReport, name='agentreports'),
    path('update_agent_location/', views.update_agent_location, name='update_agent_location'),
    path('agentfines/', views.viewFines, name='agentfines'),
] 