from django.urls import path
from accounts.views import AccountDetailView


app_name = 'accounts'

urlpatterns = [
    path('details/<int:pk>/', AccountDetailView.as_view(), name='details'),
]
