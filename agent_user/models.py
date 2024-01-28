from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    register_id = models.CharField(max_length=100)
    licenses = models.ImageField(upload_to='dash_css/images/agentimg/')
    agent_img = models.ImageField(upload_to='dash_css/images/agentimg/')
    vehicle_img = models.ImageField(upload_to='dash_css/images/agentimg/')
    username = models.CharField(max_length = 100)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    usertype = models.CharField(max_length=10, default='agent')
    latitude = models.TextField(null=True)
    longitude = models.TextField(null=True)


    def __str__(self):
        return self.name


class AgentCurrentLocation(models.Model):
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE,null=True)
    latitude = models.TextField(null=True)
    longitude = models.TextField(null=True)