from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from accounts.models import Account
from .serializers import AccountSerializer


class AccountAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response({"accounts": serializer.data})

    def post(self, request):
        account = request.data
        serializer = AccountSerializer(data=account)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get_account_object(self, pk):
        return Account.objects.get(pk=pk)

    def get(self, request, pk):
        account = self.get_account_object(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk):
        account = self.get_account_object(pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = self.get_account_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
