from banks.models import Bank
from .serializers import BankSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class BankListCreateAPI(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminUser]


class BankRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminUser]

