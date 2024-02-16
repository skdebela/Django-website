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
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return HttpResponse("news page")