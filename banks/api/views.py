from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from banks.models import Bank
from .serializers import BankSerializer


class BankAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response({"banks": serializer.data})
