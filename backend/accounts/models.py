from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movie.models import Movie

# Create your models here.
class User(AbstractUser):
    user_profile = models.TextField()
    user_liked_movie = models.ManyToManyField(Movie)