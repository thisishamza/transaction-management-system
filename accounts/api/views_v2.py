from accounts.models import Account
from .serializers import AccountSerializer
from rest_framework import generics
from core.permissions import IsCustomer, IsAccountOwnerOrReadOnly


class AccountListAPI(generics.ListAPIView):
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    serializer_class = AccountSerializer
    permission_classes = [IsCustomer]


class AccountRetrieveAPI(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer, IsAccountOwnerOrReadOnly]


class AccountCreateAPI(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer, IsAccountOwnerOrReadOnly]


class AccountUpdateAPI(generics.RetrieveUpdateAPIView, IsAccountOwnerOrReadOnly):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer, IsAccountOwnerOrReadOnly]


class AccountDeleteAPI(generics.DestroyAPIView, IsAccountOwnerOrReadOnly):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer, IsAccountOwnerOrReadOnly]
