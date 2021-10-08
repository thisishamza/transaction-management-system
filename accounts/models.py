from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class GenderChoices(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'

class Account(models.Model):
    bank = models.ForeignKey('banks.Bank', related_name='accounts', on_delete=models.PROTECT)
    user = models.ForeignKey(user, related_name='accounts', on_delete=models.PROTECT)
    account_number = models.PositiveIntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices, blank=False, null=True)
    address = models.TextField()
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account_no)
