from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Thing(AbstractUser):
    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length = 120, blank = True)
    quantity = models.IntegerField()
