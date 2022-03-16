from django.urls import path
from . import views
from accounts.views import UserListView


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path ('profile/', views.profile , name="profile"),
    path ('', views.dashboard , name="dashboard"),
	path('usersgrp/', views.AddUser, name="usersgrp"),
	path('userslist/', UserListView.as_view()),
	
]
