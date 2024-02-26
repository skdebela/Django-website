from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.genre


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre)
    album_art = models.ImageField(upload_to='')
    release_date = models.DateField()
    average_rating = models.FloatField()
    spotify_link = models.URLField()

    def __str__(self) -> str:
        return self.album_name

    def genre_list(self):
        return list(self.genre.values_list('genre', flat=True))

    def artist_list(self):
        return list(artist.name for artist in self.artists.all())


class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_writer = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    news_detail = models.TextField()
    news_image = models.ImageField(upload_to='')

    def __str__(self) -> str:
        return self.news_title


class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self) -> str:
        return self.subject
