from django.contrib import admin
from .models import Genre, Artist, Album, News, UserMessage, Review


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ['genre']  # Orders by the 'genre' field alphabetically


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    ordering = ['name']  # Orders by the 'artist' field alphabetically


admin.site.register(Album)

admin.site.register(News)

admin.site.register(UserMessage)

admin.site.register(Review)