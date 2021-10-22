from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Bank

User = get_user_model()


class TestCaseBank(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='hamza', password='123456', type='admin', is_superuser=True,
                                        is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_api_can_get_a_banklist(self):
        response = self.client.get(reverse('banks:bank-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_create_a_bank(self):
        bank_data = {'name': 'Test bank', 'created_by': self.user.id, 'modified_by': self.user.id}
        response = self.client.post(reverse('banks:bank-list'), bank_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_update_bank(self):
        bank = Bank.objects.create(name='test bank', created_by=self.user, modified_by=self.user)
        bank_data = {'name': 'Something new'}
        self.client.patch(reverse('banks:bank', kwargs={'pk': bank.id}), bank_data)
        bank_name = Bank.objects.get(id=bank.id)
        self.assertEqual(bank_data['name'], bank_name.name)

    def test_api_can_delete_bank(self):
        bank = Bank.objects.create(name='test bank', created_by=self.user, modified_by=self.user)
        self.client.delete(reverse('banks:bank', kwargs={'pk': bank.id}))
        len_of_bank_data = len(Bank.objects.filter(id=bank.id))
        self.assertEqual(len_of_bank_data, 0)
