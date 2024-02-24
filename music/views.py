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
  success = False
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    
    # Create and save a new instance of User_Messages
    user_message = User_Messages(name=name, email=email, subject=subject, message=message)
    user_message.save()
    success = True
  return render(request, 'contact.html', {'success': success})


def chart(request):
  albums = Album.objects.order_by('-average_rating')
  context = {
    'albums': albums,
  }
  return render(request, 'chart.html', context)


def new_music(request):
    albums = Album.objects.order_by('-release_date')
    latest_music = {
      'albums': albums,
    }
    return render(request, 'new_music.html', latest_music)


def news(request):
    news = News.objects.order_by('-published_date')
    news = {
        'news': news
    }
    return render(request, 'news.html', news)