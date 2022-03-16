import django_tables2 as tables
from tache.models import Tache



class TachesTable(tables.Table):
 
 

   
 class Meta:
        model = Tache
        attrs = {'id': 'taches_table'}
        template_name = "django_tables2/bootstrap.html"
        fields = ("id" , "Name", "Description" , "StartDate" , "EndDate" , "Statut"   )
        sequence = ('id','Name', 'Description' , 'StartDate' , 'EndDate' , 'Statut'  )
        