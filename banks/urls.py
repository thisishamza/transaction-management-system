from django.urls import path
from banks.api.views import BankAPIView

app_name = 'banks'

urlpatterns = [
    path('api/', BankAPIView.as_view(), name="banks_list"),
]
