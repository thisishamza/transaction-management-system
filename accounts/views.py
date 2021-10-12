from accounts.models import Account
from django.views.generic import DetailView


class AccountDetailView(DetailView):
    template_name = 'account_detail.html'
    context_object_name = 'account_details'
    model = Account
