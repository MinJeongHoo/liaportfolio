from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "core"
urlpatterns = [
    path("", views.homeview, name="home"),
    path("about", views.aboutview, name="about")
]
