from django.urls import path
from tache.views import TacheView
from tache import views


urlpatterns = [
	path('taches-list/', TacheView.as_view() , name='TachesList'),
	path('add-tache',views.AddTache , name='AddNewTache'),  
	
]
