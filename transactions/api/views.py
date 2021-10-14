from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.permissions import IsCustomer
from transactions.models import Transaction
from .serializers import TransactionSerializer


class TransactionAPIView(APIView):
    permission_classes = [IsCustomer]

    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response({"transactions": serializer.data})

    def post(self, request):
        transaction = request.data
        transaction_serializer = TransactionSerializer(data=transaction)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return Response(transaction_serializer.data)
        return Response(transaction_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailAPIView(APIView):
    permission_classes = [IsCustomer]

    def get_transaction_object(self, pk):
        return Transaction.objects.get(pk=pk)

    def get(self, request, pk):
        transaction = self.get_transaction_object(pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        transaction = self.get_transaction_object(pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = self.get_transaction_object(pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
