from django.urls import path
from .views import TransactionListView


app_name = 'transactions'

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name="transactions"),
]
