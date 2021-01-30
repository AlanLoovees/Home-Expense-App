from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
import datetime

class User(AbstractUser):
    username = models.CharField(max_length=40, null=True, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=35)

class Expense(models.Model):
    username = models.CharField(max_length=40, null=True)
    date = models.DateField(default=datetime.date.today(), blank=True)
    entryType = models.CharField(default="expense", max_length=8)
    amount = models.FloatField(default=0.00)