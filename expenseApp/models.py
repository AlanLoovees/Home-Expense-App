from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):
    username = models.CharField(max_length=40, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=35)

class Expense(models.Model):
    username = models.CharField(max_length=40, null=True)