from django.shortcuts import render

# Create your views here.

def render_login(request):
    return render(request, "auth_login.html")

def render_home(request):
    return render(request, "home.html")