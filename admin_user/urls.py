from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin_home/', views.admin_homepage, name='admin_homepage'),
     
    path('addclients/', views.addclients, name='addclients'),
    path('editclients/<str:client_id>/', views.editclients, name='editclients'),
    path('updateclient/<str:client_id>/', views.updateclient, name='updateclient'),
    path('deleteclient/<int:client_id>/', views.deleteclient, name='deleteclient'),
    path('clients/', views.clients, name='clients'),

    path('editagent/<str:agent_id>', views.editagent, name='editagent'),
    path('addagents/', views.addagents, name='addagents'),
    path('updateagent/<str:agent_id>', views.updateagent, name='updateagent'),
    path('deleteagent/<int:agent_id>/', views.deleteagent, name='deleteagent'),
    path('agents/', views.agents, name='agents'),

    path('fines/', views.fines, name='fines'),
    path('addfine/', views.addfine, name='addfines'),
    path('editfine/<str:client_id>/', views.editfine, name='editfine'),
    path('updatefine/<int:fine_id>/', views.updatefine, name='updatefine'),
    path('deletefine/<int:fine_id>/', views.deletefine, name='deletefine'),
    path('received_fines/', views.recvfines, name='receivedfines'),
    path('agentslocationadminview/', views.viewAgentsLocation, name='agentslocationadminview'),

    path('notification/', views.notify, name='notify'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)