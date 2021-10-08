from django.db import models
from django.contrib.auth.models import AbstractUser


class UserTypeChoices:
    choices = (
        (1, 'Admin'),
        (2, 'Customer'),
        (3, 'Manager'),
    )

class User(AbstractUser):
    type = models.PositiveSmallIntegerField(
        choices=UserTypeChoices.choices, blank=False, null=True)
