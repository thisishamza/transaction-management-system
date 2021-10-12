from accounts.models import Account
from transactions.models import Transaction
from django.views.generic import ListView


class TransactionListView(ListView):
    template_name = 'transactions/transaction_report.html'
    context_object_name = 'user_transactions'

    def get_queryset(self):
        account_number_list = Account.objects.filter(user=self.request.user.id).values_list('account_number', flat=True)
        transactions = Transaction.objects.filter(account__account_number__in=account_number_list)
        return transactions
