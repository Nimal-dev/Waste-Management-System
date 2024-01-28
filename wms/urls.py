
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('admin_user.urls')),
    path('', include('client_user.urls')),
    path('', include('agent_user.urls')),

]
