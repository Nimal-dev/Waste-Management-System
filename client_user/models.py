from django.db import models
from django.contrib.auth.models import User
from client_user.models import *
from agent_user.models import *
from admin_user.models import *
from agent_user.models import Agent 


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15) 
    username = models.CharField(max_length=255, null=True, blank=True)  
    location = models.TextField(null=True) 
    latitude = models.TextField(null=True)
    longitude = models.TextField(null=True)
    usertype = models.CharField(max_length=10, default='client')

    # profile_picture = models.ImageField(upload_to='dash_css/images/clientimg', null=True, blank=True)
    def __str__(self):
        return self.name
 
class Fine(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
        ('Paid', 'Paid')
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    reason = models.CharField(max_length=100)
    fined_amount = models.FloatField()
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.client.name} - {self.agent.name}"



class Notification(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null = True)
    agent = models.ForeignKey('agent_user.Agent', on_delete=models.CASCADE, null = True)
    notification_type = models.CharField(max_length=10, default='admin')
    notification_text = models.TextField(null=True)


class Completed(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null = True)
    agent = models.ForeignKey('agent_user.Agent', on_delete=models.CASCADE, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
