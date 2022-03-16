from urllib import request
from .models import Project
from django import forms
from django.contrib.auth.models import User


class AddProjectForm(forms.ModelForm):
    Title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'max-width: 300px;border: 2px solid ;margin-right: 650px;font-size: 20px',
                "placeholder": "Titre du projet",
                "class": "form-control"
            }
        ))
    Description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'style': 'max-width: 300px;border: 2px solid ;margin-right: 650px;',
                "placeholder": "Description du projet",
                "class": "form-control"
            }
        ))
    StartDate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'style': 'max-width: 300px;border: 2px solid ;margin-right: 650px;',
                "placeholder": "Date de debut",
                "class": "form-control",
                "type": "date"
            }
        ))
    EndDate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'style': 'max-width: 300px;border: 2px solid ;margin-right: 650px;',
                "placeholder": "Date de fin",
                "class": "form-control",
                "type": "date"
            }
        ))
    ProjectManager = forms.Select()

    class Meta:
        model = Project
        fields = ("Title", "Description", "StartDate", "EndDate", "ProjectManager")
