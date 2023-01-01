from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.URLField(max_length=400, blank=True)
    bio = models.TextField(blank=True)