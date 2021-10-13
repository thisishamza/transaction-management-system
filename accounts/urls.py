from django.urls import path
from accounts.views import AccountDetailView
from accounts.api.views import AccountAPIView, AccountDetailAPIView
from accounts.api.views_v2 import AccountRetrieveAPI, AccountListAPI, AccountCreateAPI, AccountUpdateAPI, \
    AccountDeleteAPI
from accounts.api.views_v3 import AccountListCreateAPI, AccountRetrieveUpdateDestroyAPI

app_name = 'accounts'

urlpatterns = [
    path('details/<int:pk>/', AccountDetailView.as_view(), name='details'),

    path('api/v1', AccountAPIView.as_view()),
    path('api/v1/<int:pk>', AccountDetailAPIView.as_view()),
    path('api/v2', AccountListAPI.as_view()),
    path('api/v2/create', AccountCreateAPI.as_view()),
    path('api/v2/retrieve/<int:pk>', AccountRetrieveAPI.as_view()),
    path('api/v2/update/<int:pk>', AccountUpdateAPI.as_view()),
    path('api/v2/delete/<int:pk>', AccountDeleteAPI.as_view()),
    path('api/v3', AccountListCreateAPI.as_view()),
    path('api/v3/<int:pk>', AccountRetrieveUpdateDestroyAPI.as_view()),

]
