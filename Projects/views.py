from ast import Add
from django.shortcuts import redirect, render
from .forms import AddProjectForm
from .tables import ProjectTable
from .models import Project
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic import DetailView


def AddProject(request):
    form = AddProjectForm()
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Addproject')
    context = {'form': form}
    return render(request, 'projects/project.html', context)


class SampleTable(View):

    def get(self, request):
        queryset = Project.objects.all()
        project_table = ProjectTable(queryset)
        context = {'view_project': project_table}
        return render(request, 'projects/projects_list.html', context)

    def post(self, request):
        pass


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DeleteProjectView(DeleteView):
    model = Project
    success_url = reverse_lazy('ProjectsList')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class UpdateProjectView(UpdateView):
    model = Project
    fields = ["Title", "Description", "StartDate", "EndDate", "ProjectManager"]
    template_name = 'projects/update_project.html'
    context_object_name = 'projet'

    def form_valid(self, form):
        projet = form.save(commit=False)
        projet.save()
        return redirect('ProjectsList')
