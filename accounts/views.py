from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import  CreateUserForm 
from .forms import AddUserForm
from django_tables2 import SingleTableView
from .tables import UserTable


@login_required(login_url='login')
def dashboard(request):
  return render (request , 'accounts/dashboard.html')



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.cleaned_data.get('username')
				form.save()
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, 'accounts/profile.html')



def AddUser(request):
	form = AddUserForm()
	if  request.method == 'POST':
			form = AddUserForm(request.POST)
			if form.is_valid():
				form.save()
				
			return redirect('usersgrp')
			
	context = {'form':form}
	return render(request, 'accounts/users_grp.html', context)




class UserListView(SingleTableView):
    model = AppUser
    table_class = UserTable
    template_name = 'accounts/users_list.html'


