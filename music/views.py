from django.contrib.sites import requests
from django.shortcuts import render
from .models import Album, News, UserMessage, Review
from django.db.models import Exists, OuterRef, Subquery


def home(request):
    # Query to fetch albums with reviews
    albums_with_reviews = Album.objects.filter(
        Exists(Review.objects.filter(album=OuterRef('pk')))
    ).annotate(
        latest_review=Subquery(
            Review.objects.filter(album=OuterRef('pk')).order_by('-published_date').values('review')[:1]
        ),
        reviewer=Subquery(
            Review.objects.filter(album=OuterRef('pk')).order_by('-published_date').values('user')[:1]
        ),
        reviewer_rating=Subquery(
            Review.objects.filter(album=OuterRef('pk')).order_by('-published_date').values('rating')[:1]
        ),
        review_published_date=Subquery(
            Review.objects.filter(album=OuterRef('pk')).order_by('-published_date').values('published_date')[:1]
        ),
    )

    context = {
        'albums': albums_with_reviews,
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
        user_message = UserMessage(name=name, email=email, subject=subject, message=message)
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
    context = {
        'news': news
    }
    return render(request, 'news.html', context)
