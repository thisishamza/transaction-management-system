from django.db import models


class TransactionTypes(models.TextChoices):
    DEBIT = 'debit'
    CREDIT = 'credit'

class Transaction(models.Model):
    account = models.ForeignKey('accounts.Account', related_name='transactions', on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    type = models.CharField(choices=TransactionTypes.choices, max_length=10, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
