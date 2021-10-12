from accounts.models import Account
from django.views.generic import ListView


class TransactionListView(ListView):
    template_name = 'transactions/transaction_report.html'
    context_object_name = 'user_transactions'

    def get_queryset(self):
        account = Account.objects.get(pk=self.request.user.id)
        return account.transactions.all()
