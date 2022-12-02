from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Things(AbstractUser):
    name = models.CharField(unique = True, blank = True, max_length = 30)
    desciption = models.CharField(max_length=120)
    quantity = models.IntegerField()
