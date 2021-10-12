from accounts.models import Account
from transactions.models import Transaction
from django.views.generic import ListView


class TransactionListView(ListView):
    template_name = 'transactions/transaction_report.html'
    context_object_name = 'user_transactions'

    def get_queryset(self):
        transactions=Transaction.objects.filter(account__user=self.request.user)
        return transactions
