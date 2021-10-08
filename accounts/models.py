from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class GenderChoices:
    choices = (
        (1, 'Male'),
        (2, 'Female'),
    )


class Account(models.Model):
    bank = models.ForeignKey('banks.Bank', related_name='accounts', on_delete=models.CASCADE)
    user = models.OneToOneField(user, related_name='accounts', on_delete=models.CASCADE)
    account_no = models.PositiveIntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices, blank=False, null=True)
    address = models.TextField()
    inital_balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account_no)
