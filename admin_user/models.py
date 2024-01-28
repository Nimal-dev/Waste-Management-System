from django.db import models

# Create your models here
class Admin(models.Model):
    email = models.EmailField(null=True)
    name = models.CharField(max_length=20, null=True)
    admin_img = models.ImageField(upload_to='dash_css/images/adminimg/', null = True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name
    
