from client_user.models import *
from agent_user.models import *
from admin_user.models import *

def getNotifications(request): 
    if(request.user.is_authenticated): 
        if(hasattr(request.user, 'client')):
            notifications = Notification.objects.filter(client=request.user.client).order_by('-id')
        else:
            notifications={}
    else:
        notifications={}
    return {
        'notifications': notifications
    }