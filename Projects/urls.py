from django.urls import path
from . import views
from Projects.views import SampleTable
from Projects.views import DeleteProjectView
from Projects.views import UpdateProjectView
from Projects.views import ProjectDetailView

urlpatterns = [
    path('add-project/', views.AddProject, name='Addproject'),
    path('projects-list/', SampleTable.as_view(), name='ProjectsList'),
    path('delete-project/<int:pk>/', DeleteProjectView.as_view(), name='delete_project'),
    path('update-project/<int:pk>/', UpdateProjectView.as_view(), name='update_project'),
    path('project-details/<int:pk>/', ProjectDetailView.as_view(), name='project_details')
]
