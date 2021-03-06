from transactions.models import Transaction
from .serializers import TransactionSerializer
from rest_framework import generics
from core.permissions import IsCustomer, IsTransactionOwnerOrReadOnly


class TransactionListAPI(generics.ListAPIView):
    def get_queryset(self):
        return Transaction.objects.filter(account__user=self.request.user)

    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer]


class TransactionRetrieveAPI(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer, IsTransactionOwnerOrReadOnly]


class TransactionCreateAPI(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer, IsTransactionOwnerOrReadOnly]


class TransactionUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer, IsTransactionOwnerOrReadOnly]


class TransactionDeleteAPI(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsCustomer, IsTransactionOwnerOrReadOnly]
