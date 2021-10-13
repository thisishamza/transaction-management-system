from django.urls import path
from .views import TransactionListView
from transactions.api.views import TransactionAPIView, TransactionDetailAPIView
from transactions.api.views_v2 import TransactionRetrieveAPI, TransactionListAPI, TransactionCreateAPI, \
    TransactionUpdateAPI, TransactionDeleteAPI
from transactions.api.views_v3 import TransactionListCreateAPI, TransactionRetrieveUpdateDestroyAPI

app_name = 'transactions'

urlpatterns = [
    path('', TransactionListView.as_view(), name="transaction"),

    path('api/v1', TransactionAPIView.as_view()),
    path('api/v1/<int:pk>', TransactionDetailAPIView.as_view()),
    path('api/v2', TransactionListAPI.as_view()),
    path('api/v2/create', TransactionCreateAPI.as_view()),
    path('api/v2/retrieve/<int:pk>', TransactionRetrieveAPI.as_view()),
    path('api/v2/update/<int:pk>', TransactionUpdateAPI.as_view()),
    path('api/v2/delete/<int:pk>', TransactionDeleteAPI.as_view()),
    path('api/v3', TransactionListCreateAPI.as_view()),
    path('api/v3/<int:pk>', TransactionRetrieveUpdateDestroyAPI.as_view()),

]
