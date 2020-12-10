from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def homeview(request):
    return render(request, "home.html")


def aboutview(request):
    return render(request, "about.html")
