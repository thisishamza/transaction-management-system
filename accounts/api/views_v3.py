from accounts.models import Account
from .serializers import AccountSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, BasePermission


class CustomerAccessPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        if request.user.type == 'customer':
            return True


class AccountListCreateAPI(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [CustomerAccessPermission]


class AccountRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser, CustomerAccessPermission]
