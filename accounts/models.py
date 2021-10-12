from django.db import models
from django.contrib.auth import get_user_model
from core.models import AuditFieldMixin, SoftDeleteMixin


user = get_user_model()


class GenderChoices(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'


class Account(AuditFieldMixin, SoftDeleteMixin):
    bank = models.ForeignKey('banks.Bank', related_name='accounts', on_delete=models.PROTECT)
    user = models.ForeignKey(user, related_name='accounts', on_delete=models.PROTECT)
    account_number = models.PositiveIntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GenderChoices.choices, max_length=20)
    address = models.TextField()
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.account_number}'
