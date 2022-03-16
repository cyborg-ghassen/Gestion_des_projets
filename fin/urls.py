from django.contrib import admin
from django.urls import path, include
from django.urls import path  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('Projects.urls')),
    path('', include('tache.urls')),
    
]