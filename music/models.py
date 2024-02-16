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
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    album_art = models.ImageField(upload_to='')
    release_date = models.DateField()
    spotify_link = models.URLField()

    def __str__(self) -> str:
        return self.album_name

    def genre_list(self):
        return list(self.genre.values_list('genre', flat=True))