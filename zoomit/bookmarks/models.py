from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class UrlObject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.url
