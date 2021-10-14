from accounts.models import Account
from .serializers import AccountSerializer
from rest_framework import generics
from core.permissions import IsCustomer


class AccountListAPI(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer]


class AccountRetrieveAPI(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer]


class AccountCreateAPI(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer]


class AccountUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer]


class AccountDeleteAPI(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer]
