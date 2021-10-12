from django.db import models
from django.contrib.auth.models import AbstractUser


class UserTypeChoices(models.TextChoices):
    ADMIN = 'admin'
    CUSTOMER = 'customer'
    MANAGER = 'manager'


class User(AbstractUser):
    type = models.CharField(choices=UserTypeChoices.choices, max_length=20)
