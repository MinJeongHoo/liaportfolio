from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "works"
urlpatterns = [
    path("", views.worksview, name="works"),
    path("<int:pk>", views.worksview, name="desc")
]
