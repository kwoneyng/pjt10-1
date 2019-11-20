from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=40)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies') # 유저입장에서 


class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)  # 
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)


