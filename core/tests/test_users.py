from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class UsersApiTestCase(APITestCase):
    def test_create_user(self):
        user_data = {
            'username': 'username',
            'email': 'username1@mail.com',
            'password': '123456'
        }
        result = self.client.post('/api/v1/users/', user_data)
        assert result.status_code == 201
