from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class ActionsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'test_user@mail.com', '123456')
        self.useradmin = User.objects.create_superuser('test_admin', 'admin@admin.com', '123456')

    def test_students(self):
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})
        token = result.data['access']
        students = self.client.get('/api/v1/users/students/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        role = students.data[0]['is_staff']
        assert students.status_code == 200
        assert role == False

    def test_admin(self):
        result = self.client.post('/api/token/', {'username': 'test_admin', 'password': '123456'})
        token = result.data['access']
        admins = self.client.get('/api/v1/users/isadmin/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        role = admins.data[0]['is_staff']
        assert admins.status_code == 200
        assert role == True
