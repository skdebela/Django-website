# Generated by Django 5.0.2 on 2024-02-24 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_rename_artist_album_album_artist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_artist',
            new_name='artists',
        ),
    ]
