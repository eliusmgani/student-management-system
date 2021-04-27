from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from students.EmailBackEnd import EmailBackEnd
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
	return render(request, "home.html")


def loginpage(request):
	return render(request, "login.html")

def dologin(request):
	if request.method != "POST":
		return HttpResponse("<h2>Method is Not Allowed..!!</h2>")
	else:
		user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
		if user != None:
			login(request, user)
			if user.user_type=="1":
				return HttpResponseRedirect("/adminhome")
			elif user.user_type=="2":
				return HttpResponseRedirect(reverse("StaffHome"))
			else:
				return HttpResponseRedirect(reverse("StudentHome"))
		else:
			messages.error(request, f'Invalid Login Details..!!')
			return HttpResponseRedirect("/")


def getuserdetails(request):
	if request.user !=None:
		return HttpResponse("user: "+request.user.email+" user_type: "+request.user_type)
	else:
		return HttpResponse("<h2>Please Login First</h2>")


def logoutuser(request):
	logout(request)
	return HttpResponseRedirect('/')
