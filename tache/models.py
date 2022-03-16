from django.db import models

class Tache(models.Model):
   Name = models.CharField(max_length=255 , verbose_name='Nom')    
   Description = models.TextField( max_length=800 , verbose_name='Description du tache')
   StartDate  = models.DateField(  max_length=100, auto_now=False, auto_now_add=False , verbose_name='Date de début') 
   EndDate = models.DateField( max_length=100, auto_now=False, auto_now_add=False, verbose_name='Date de fin')
   Statut = models.CharField(max_length=100 , verbose_name='Statut du tache')
   

   
   