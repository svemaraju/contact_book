import datetime

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient



class RegisterUserTests(APITestCase):
    def setUp(self):
        self.url = reverse(
            'contact_book.users.register',
            kwargs={'format': 'json'}
        )

    def test_register(self):
        data = {
            'first_name': 'Barret',
            'last_name': 'Wallace',
            'email': 'testuser@gmail.com',
            'password': '1234567890'
        }

        response = self.client.post(
            self.url, data, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


