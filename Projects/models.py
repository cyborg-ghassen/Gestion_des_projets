from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Project(models.Model):
    Title = models.CharField(max_length=255, verbose_name='Titre du projet')
    Description = models.TextField(max_length=800, verbose_name='Description du projet')
    StartDate = models.DateField(max_length=100, auto_now=False, auto_now_add=False, verbose_name='Date de début')
    EndDate = models.DateField(max_length=100, auto_now=False, auto_now_add=False, verbose_name='Date de fin')
    ProjectManager = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('project_details', kwargs={'pk': self.id})

    def get_delete_project_url(self):
        return reverse('delete_project', kwargs={'pk': self.id})

    def get_update_project_url(self):
        return reverse('update_project', kwargs={'pk': self.id})
