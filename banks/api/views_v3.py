from banks.models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer
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


class BranchListCreateAPI(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]


class BranchRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]
