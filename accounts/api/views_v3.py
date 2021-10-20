from accounts.models import Account
from .serializers import AccountSerializer
from rest_framework import generics
from core.permissions import IsCustomer
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "Owner can only view and edit this data"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class AccountListCreateAPI(generics.ListCreateAPIView):
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    serializer_class = AccountSerializer
    permission_classes = [IsCustomer, IsAuthenticatedOrReadOnly]


class AccountRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsCustomer, IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
