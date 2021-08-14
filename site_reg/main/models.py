from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    password1 = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'


# class User(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=100, default='')
#     last_name = models.CharField(max_length=100, default='')
#     email = models.EmailField(blank=True)
#     phone = models.IntegerField(default=0)
#     password = models.CharField(max_length=30)
#     password1 = models.CharField(max_length=30)
#
#     USERNAME_FIELD = 'username'


# class User(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     email = models.CharField(max_length=30)
#     phone_number = models.CharField(max_length=11)
#     password = models.CharField(max_length=30)