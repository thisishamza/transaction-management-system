from transactions.models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics
from core.permissions import IsCustomer, IsTransactionOwnerOrReadOnly


class TransactionListCreateAPI(generics.ListCreateAPIView):
    def get_queryset(self):
        transactions = Transaction.objects.filter(account__user=self.request.user)
        return transactions

    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]


class TransactionRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView, IsTransactionOwnerOrReadOnly):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer, IsTransactionOwnerOrReadOnly]
