from transactions.models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics
from core.permissions import IsCustomer


class TransactionListAPI(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]


class TransactionRetrieveAPI(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]


class TransactionCreateAPI(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]


class TransactionUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]


class TransactionDeleteAPI(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]
