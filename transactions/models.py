from django.db import models


class TransactionTypes:
    choices = (
        (1, 'Debit'),
        (2, 'Credit'),
    )


class Transaction(models.Model):
    account = models.ForeignKey('accounts.Account', related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    type = models.PositiveSmallIntegerField(choices=TransactionTypes.choices, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'
