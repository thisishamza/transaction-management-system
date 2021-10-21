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
        self.bank_data = {'name': 'Test bank', 'created_by': self.user.id, 'modified_by': self.user.id}

    def test_api_can_get_a_banklist(self):
        response = self.client.get(reverse('banks:bank-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_create_a_bank(self):
        response = self.client.post(reverse('banks:bank-list'), self.bank_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_update_bank(self):
        self.client.post(reverse('banks:bank-list'), self.bank_data)
        bank = Bank.objects.first()
        self.bank_data.update({'name': 'Something new'})
        res = self.client.put(reverse('banks:bank', kwargs={'pk': bank.id}), self.bank_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bank(self):
        self.client.post(reverse('banks:bank-list'), self.bank_data)
        bank = Bank.objects.first()
        response = self.client.delete(reverse('banks:bank', kwargs={'pk': bank.id}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
