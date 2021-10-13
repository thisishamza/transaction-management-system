from accounts.models import Account
from .serializers import AccountSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class AccountListCreateAPI(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]


class AccountRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]
