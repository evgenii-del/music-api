from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    musician = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="albums/", default='tracks/album.jpeg')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Track(models.Model):
    musician = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    track = models.FileField(upload_to="music")
    image = models.ImageField(upload_to="tracks/", default='tracks/music.jpg')
    slug = models.SlugField(max_length=150)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    album = models.ForeignKey(Album, blank=True, null=True, on_delete=models.SET_NULL, related_name="tracks")

    def __str__(self):
        return self.title
