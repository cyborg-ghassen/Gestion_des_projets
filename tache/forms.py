from tache.models import Tache
from django import forms 

class AddTacheForm(forms.ModelForm):  
    class Meta:  
        model = Tache
        fields = ['Name', 'Description', 'StartDate' , 'EndDate' , 'Statut'] 
        widgets = { 'Name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'Description': forms.Textarea(attrs={ 'class': 'form-control' }),
            'StartDate': forms.DateInput(attrs={ 'class': 'form-control' , 'type' : 'date' }),
            'EndDate': forms.DateInput(attrs={ 'class': 'form-control' , 'type' : 'date' }),
             'Statut': forms.TextInput(attrs={ 'class': 'form-control'  }),
             }