import django_tables2 as tables
from .models import Project





class ProjectTable(tables.Table):
 Details = tables.TemplateColumn('<a href="{{ record.get_absolute_url }}" class="btn btn-info"><i class="fa fa-edit"></i></a>', orderable=False)  
 Edit = tables.TemplateColumn('<a href="{{ record.get_update_project_url }}" class="btn btn-info"><i class="fa fa-edit"></i></a>', orderable=False)
 Delete = tables.TemplateColumn('<a href="{{ record.get_delete_project_url }}" class="btn btn-info"><i class="fa fa-edit"></i></a>', orderable=False)  

   
 class Meta:
        model = Project
        attrs = {'id': 'projects_table'}
        template_name = "django_tables2/bootstrap.html"
        fields = ("id" , "Title", "Description" , "StartDate" , "EndDate" , "ProjectManager"   )
        sequence = ('id','Title', 'Description' , 'StartDate' , 'EndDate' , 'ProjectManager'  )
        
        

    
        
    
    