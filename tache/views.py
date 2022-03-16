from django.shortcuts import redirect, render 
from tache.models import Tache
from tache.tables import TachesTable
from django.views.generic.base import View
from tache.forms import AddTacheForm



class TacheView(View):


    def get(self,request):

        queryset = Tache.objects.all()
        taches_table = TachesTable(queryset)
        context = {'view_taches':taches_table}
        return render(request, 'taches/taches_list.html', context)

    def post(self,request):

        pass

def AddTache(request):
	form = AddTacheForm()
	if  request.method == 'POST':
			form = AddTacheForm(request.POST)
			if form.is_valid():
				form.save()
				
			return redirect('/')
			
	context = {'form':form}
	return render(request, 'taches/add_tache.html', context)

