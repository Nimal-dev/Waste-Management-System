# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms


# from django.contrib.auth.models import User

# class CreateUserForm(forms.UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','email', 'password1', 'password2']

#         widgets={'name'forms.TextInput(attrs={'class':'form-control'})}
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
