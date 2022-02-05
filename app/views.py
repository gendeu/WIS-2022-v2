from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def render_login(request):
    return render(request, "auth_login.html")

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("render_home"))
        else:
            messages.error(request, "Username or Password is Invalid!")
            return HttpResponseRedirect("/")        
            
def render_home(request):
    return render(request, "home.html")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")