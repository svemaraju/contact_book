import datetime

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from contact_book.contacts.factory import ContactFactory
from contact_book.users.factory import UserFactory


class ContactTestCase(APITestCase):

    def setUp(self):
        # set up Test User 1
        self.test_user_1 = UserFactory.create()
        self.test_client_1 = APIClient()
        self.test_client_1.force_authenticate(user=self.test_user_1)

        # set up Test User 2
        self.test_user_2 = UserFactory.create()
        self.test_client_2 = APIClient()
        self.test_client_2.force_authenticate(user=self.test_user_2)


    def create_test_contacts(self):
        # create a random set of contacts 
        # for test_user_1
        return [ContactFactory(holder=self.test_user_1)
            for i in range(10)]



    def test_contact_creation(self):
        url = reverse(
            'contact_book.contacts.',
            kwargs={'format': 'json'}
        )
        data = {
            'name': 'James Bond',
            'email': '007@secretservice.co.uk',
            'mobile': '+1-617-806-6434'

        }
        response = self.test_client_1.post(
            url, 
            data, 
            format='json'
        )
        # Test a contact creation.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            'name': 'James Bond',
            'email': '007@secretservice.co.uk',
            'mobile': '+1-617-806-6434'

        }
        response = self.test_client_1.post(
            url, 
            data, 
            format='json'
        )
        # Test a duplicate contact creation
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_search_with_email(self):
        test_contacts = self.create_test_contacts()
        
        email = test_contacts[0].email
        
        url = reverse(
            'contact_book.contacts.',
            kwargs={'format': 'json'}
        )
        params = {'email': email}
        response = self.test_client_1.get(
            url, 
            params, 
            format='json'
        )
        # Positive search results.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

        params = {'email': 'random.nonexistingemail@gmail.com'}
        response = self.test_client_1.get(
            url, 
            params, 
            format='json'
        )
        # Negative/Empty search results.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 0)


    def test_search_with_name(self):
        test_contacts = self.create_test_contacts()
        
        name = test_contacts[0].name
        
        url = reverse(
            'contact_book.contacts.',
            kwargs={'format': 'json'}
        )
        params = {'name': name}
        response = self.test_client_1.get(
            url, 
            params, 
            format='json'
        )
        # Positive search results.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)



    def test_update_contact(self):
        test_contact_1 = ContactFactory(holder=self.test_user_1)
        pk = test_contact_1.pk
        url = reverse(
            'contact_book.contacts.detail',
            kwargs={'format': 'json', 'pk':pk}
        )

        changed_name = 'Changed Name'
        data = {'name': changed_name}
        response = self.test_client_1.patch(
            url, 
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], changed_name)


    def test_delete_contact(self):
        test_contact_1 = ContactFactory(holder=self.test_user_1)
        pk = test_contact_1.pk
        url = reverse(
            'contact_book.contacts.detail',
            kwargs={'format': 'json', 'pk':pk}
        )

        changed_name = 'Changed Name'
        data = {'name': changed_name}
        response = self.test_client_1.delete(
            url
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Test by calling Contact Detail 
        response = self.test_client_1.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




