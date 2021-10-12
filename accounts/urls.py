from django.urls import path
from accounts.views import AccountDetailView


app_name = 'accounts'

urlpatterns = [
    path('detail/<pk>/', AccountDetailView.as_view(), name='details'),
]
