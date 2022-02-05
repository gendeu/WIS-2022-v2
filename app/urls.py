from django.urls import path
from app import views

urlpatterns = [
    path("", views.render_login, name="render_login"),
    path("login", views.perform_login, name="perform_login"),
    path("home", views.render_home, name="render_home"),
    path("logout", views.perform_logout, name="perform_logout")
]
