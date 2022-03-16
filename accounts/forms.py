from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AppUser 
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class AddUserForm(forms.ModelForm):
    FirstName = forms.CharField(
        widget=forms.TextInput(
            attrs={
               'style': 'max-width: 300px;border: 2px solid ;margin-right: 650px;',
                "placeholder": "Nom",
                "class": "form-control"
            }
        ))
    LastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
              'style': 'max-width: 300px;border: 2px solid ;margin-right: 650px;',
                "placeholder": "Prenom",
                "class": "form-control"
            }
        ))
    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
              'style': 'max-width: 300px;border: 2px solid ;margin-right: 650px;',
                "placeholder": "Adresse-Email",
                "class": "form-control"
            }
        ))
   
      

    class Meta:
        model = AppUser
        fields = '__all__'


