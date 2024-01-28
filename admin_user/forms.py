# forms.py

from django import forms
from client_user.models import Fine

class FineForm(forms.ModelForm):
    class Meta:
        model = Fine
        fields = ['client', 'agent', 'reason', 'fined_amount', 'status']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
            'fined_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


