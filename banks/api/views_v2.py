from banks.models import Bank
from .serializers import BankSerializer
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
