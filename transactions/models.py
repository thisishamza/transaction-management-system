from django.db import models
from core.models import AuditFieldMixin, SoftDeleteMixin


class TransactionTypes(models.TextChoices):
    DEBIT = 'debit'
    CREDIT = 'credit'


class Transaction(AuditFieldMixin, SoftDeleteMixin):
    account = models.ForeignKey('accounts.Account', related_name='transactions', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(choices=TransactionTypes.choices, max_length=20)

    def __str__(self):
        return f'{self.id}'
