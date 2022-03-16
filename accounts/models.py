from django.db import models



class AppUser(models.Model):
 User_type=(
('1', 'Chef Du Projet'),
('2', 'Utilisateur'),
('3', 'Client'),

 )  
 FirstName = models.CharField(max_length=255)
 LastName = models.CharField(max_length=255)
 Email = models.EmailField(max_length=255 )
 Type = models.CharField(max_length=100,choices=User_type , default="Chef Du Projet")




