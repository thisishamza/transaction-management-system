from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from banks.models import Bank
from .serializers import BankSerializer


class BankAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response({"banks": serializer.data})

    def post(self, request):
        bank = request.data
        bank_serializer = BankSerializer(data=bank)
        if bank_serializer.is_valid():
            bank_serializer.save()
            return Response(bank_serializer.data)
        return Response(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BankDetailAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get_bank_object(self, pk):
        return Bank.objects.get(pk=pk)

    def get(self, request, pk):
        bank = self.get_bank_object(pk)
        serializer = BankSerializer(bank)
        return Response(serializer.data)

    def put(self, request, pk):
        bank = self.get_bank_object(pk)
        serializer = BankSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bank = self.get_bank_object(pk)
        try:
            bank.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'Bank cannot be deleted.Delete the related bank accounts first'})
