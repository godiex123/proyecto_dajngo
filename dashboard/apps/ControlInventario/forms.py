from django import forms
from apps.ControlInventario.models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','password','email')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-user','id':'exampleFirstName','placeholder': 'First Name'})
        }