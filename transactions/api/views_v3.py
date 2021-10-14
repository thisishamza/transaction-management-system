from transactions.models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics
from core.permissions import IsCustomer


class TransactionListCreateAPI(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]


class TransactionRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]
