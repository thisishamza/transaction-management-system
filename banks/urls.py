from django.urls import path
from banks.api.views import BankAPIView, BankDetailAPIView
from banks.api.views_v2 import BankRetrieveAPI, BankListAPI, BankCreateAPI, BankUpdateAPI, BankDeleteAPI
from banks.api.views_v3 import BankListCreateAPI, BankRetrieveUpdateDestroyAPI


app_name = 'banks'

urlpatterns = [
    path('api/v1', BankAPIView.as_view()),
    path('api/v1/<int:pk>', BankDetailAPIView.as_view()),

    path('api/v2', BankListAPI.as_view()),
    path('api/v2/create', BankCreateAPI.as_view()),
    path('api/v2/retrieve/<int:pk>', BankRetrieveAPI.as_view()),
    path('api/v2/update/<int:pk>', BankUpdateAPI.as_view()),
    path('api/v2/delete/<int:pk>', BankDeleteAPI.as_view()),

    path('api/v3', BankListCreateAPI.as_view()),
    path('api/v3/<int:pk>', BankRetrieveUpdateDestroyAPI.as_view()),

]
