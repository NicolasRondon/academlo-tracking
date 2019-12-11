from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class WorkspaceTestCase(APITestCase):
    def setUp(self):
        self.useradmin = User.objects.create_superuser('test_admin', 'admin@admin.com', '123456')

    def test_users_action_get(self):
        result = self.client.post('/api/token/', {'username': 'test_admin', 'password': '123456'})
        token = result.data['access']
        workspace = self.client.post('/api/v1/workspace/',
                                     {'name': 'name', 'description': 'nueva descripcion',
                                      'users': '1'},
                                     HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        users = self.client.get('/api/v1/workspace/1/users/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert users.status_code == 200

    def test_user_action_delete(self):
        result = self.client.post('/api/token/', {'username': 'test_admin', 'password': '123456'})
        token = result.data['access']
        workspace = self.client.post('/api/v1/workspace/',
                                     {'name': 'name', 'description': 'nueva descripcion',
                                      'users': '1'},
                                     HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        users = self.client.delete('/api/v1/workspace/1/users/', {'id': '1'},
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert users.status_code == 200

    def test_user_action_post(self):
        result = self.client.post('/api/token/', {'username': 'test_admin', 'password': '123456'})
        token = result.data['access']
        workspace = self.client.post('/api/v1/workspace/',
                                     {'name': 'name', 'description': 'nueva descripcion',
                                      'users': '1'},
                                     HTTP_AUTHORIZATION='Bearer {0}'.format(token))

        users = self.client.delete('/api/v1/workspace/1/users/', {'id': '1'},
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(token))

        usersp =self.client.post('/api/v1/workspace/1/users/', {'id': '1'},
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(token))

        assert usersp.status_code == 200