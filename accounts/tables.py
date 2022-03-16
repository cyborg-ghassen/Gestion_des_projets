import django_tables2 as tables
from .models import AppUser

class UserTable(tables.Table):
    class Meta:
        model = AppUser
        template_name = "django_tables2/bootstrap.html"
        fields = ("FirstName", "LastName" , "Email" )


        