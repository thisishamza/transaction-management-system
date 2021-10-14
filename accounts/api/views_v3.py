from accounts.models import Account
from .serializers import AccountSerializer
from rest_framework import generics
from core.permissions import IsCustomer


class AccountListCreateAPI(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer]


class AccountRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer]
