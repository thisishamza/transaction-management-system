from banks.models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class BankListAPI(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminUser]


class BankRetrieveAPI(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminUser]


class BankCreateAPI(generics.CreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminUser]


class BankUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminUser]


class BankDeleteAPI(generics.DestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [IsAdminUser]


class BranchListAPI(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]


class BranchRetrieveAPI(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]


class BranchCreateAPI(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]


class BranchUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]


class BranchDeleteAPI(generics.DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]
