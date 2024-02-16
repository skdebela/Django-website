from django.contrib.sites import requests
from django.shortcuts import render, HttpResponse
from .models import *


def home(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'home.html', context)


def about(request):
    return HttpResponse("about page")


def contact(request):
    return HttpResponse("contact page")


def news(request):
    return HttpResponse("news page")