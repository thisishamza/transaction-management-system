from django.urls import path
from banks.api.views import BankAPIView, BankDetailAPIView
from banks.api.views_v2 import BankRetrieveAPI, BankListAPI, BankCreateAPI, BankUpdateAPI, BankDeleteAPI
from banks.api.views_v3 import BankListCreateAPI, BankRetrieveUpdateDestroyAPI
from banks.api.views import BranchAPIView, BranchDetailAPIView
from banks.api.views_v2 import BranchRetrieveAPI, BranchListAPI, BranchCreateAPI, BranchUpdateAPI, BranchDeleteAPI
from banks.api.views_v3 import BranchListCreateAPI, BranchRetrieveUpdateDestroyAPI

app_name = 'banks'

urlpatterns = [

    path('api/v1', BankAPIView.as_view()),
    path('api/v1/<int:pk>', BankDetailAPIView.as_view()),
    path('api/v2', BankListAPI.as_view()),
    path('api/v2/create', BankCreateAPI.as_view()),
    path('api/v2/retrieve/<int:pk>', BankRetrieveAPI.as_view()),
    path('api/v2/update/<int:pk>', BankUpdateAPI.as_view()),
    path('api/v2/delete/<int:pk>', BankDeleteAPI.as_view()),
    path('api/v3', BankListCreateAPI.as_view(), name="bank-list"),
    path('api/v3/<int:pk>', BankRetrieveUpdateDestroyAPI.as_view(), name="bank"),

    path('branch/api/v1', BranchAPIView.as_view()),
    path('branch/api/v1/<int:pk>', BranchDetailAPIView.as_view()),
    path('branch/api/v2', BranchListAPI.as_view()),
    path('branch/api/v2/create', BranchCreateAPI.as_view()),
    path('branch/api/v2/retrieve/<int:pk>', BranchRetrieveAPI.as_view()),
    path('branch/api/v2/update/<int:pk>', BranchUpdateAPI.as_view()),
    path('branch/api/v2/delete/<int:pk>', BranchDeleteAPI.as_view()),
    path('branch/api/v3', BranchListCreateAPI.as_view()),
    path('branch/api/v3/<int:pk>', BranchRetrieveUpdateDestroyAPI.as_view()),

]
