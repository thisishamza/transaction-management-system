from django.urls import path
from banks.api.views import BankAPIView, BankDetailAPIView

app_name = 'banks'

urlpatterns = [
    path('api', BankAPIView.as_view()),
    path('api/<int:pk>', BankDetailAPIView.as_view()),
]
