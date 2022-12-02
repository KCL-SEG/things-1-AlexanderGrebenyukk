from django.db import models
from django.contrib.auth.models import AbstractUser
import django.db.models.Model
# Create your models here.
class Thing(AbstractUser):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 120)
    quantity = models.IntegerField()
