from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    basic = models.BooleanField('basic status', default=False)
    premium = models.BooleanField('premium status', default=False)
    enterprise = models.BooleanField('enterprise status', default=False)