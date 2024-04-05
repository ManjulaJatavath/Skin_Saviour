from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.helpers.timestamp_model import TimeStampedModel
# Create your models here.

class User(AbstractUser, TimeStampedModel):
    email = models.EmailField(unique=True)