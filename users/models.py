from django.db import models
from django.contrib.auth.models import AbstractUser


class UserTypeChoices(models.TextChoices):
    ADMIN = 'admin'
    CUSTOMER = 'customer'
    MANAGER = 'manager'


class User(AbstractUser):
    type = models.PositiveSmallIntegerField(
        choices=UserTypeChoices.choices, blank=False, null=True)
