# Generated by Django 5.0.2 on 2024-02-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_rename_emain_user_messages_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(to='music.artist'),
        ),
    ]
