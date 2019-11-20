from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Customizing User model
class User(AbstractUser):
    followers = models.ManyToManyField( # followers: 나를 팔로우하는 사람들
        settings.AUTH_USER_MODEL,
        related_name='followings'       # followings: 내가 팔로우하는 사람들
    )

    