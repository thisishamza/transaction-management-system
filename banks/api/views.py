from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from banks.models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer


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


class BranchAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response({"banks": serializer.data})

    def post(self, request):
        branch = request.data
        branch_serializer = BranchSerializer(data=branch)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return Response(branch_serializer.data)
        return Response(branch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchDetailAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get_branch_object(self, pk):
        return Branch.objects.get(pk=pk)

    def get(self, request, pk):
        branch = self.get_branch_object(pk)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

    def put(self, request, pk):
        branch = self.get_branch_object(pk)
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        branch = self.get_branch_object(pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
