from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class WorkspaceTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('test_admin', 'admin@admin.com', '123456')

    def test_admin_workspace_get(self):
        result = self.client.post('/api/token/', {'username': 'test_admin', 'password': '123456'})
        token = result.data['access']
        workspaces = self.client.get('/api/v1/workspace/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert workspaces.status_code == 200

    def test_admin_workspace_create(self):
        result = self.client.post('/api/token/', {'username': 'test_admin', 'password': '123456'})
        token = result.data['access']
        workspace = self.client.post('/api/v1/workspace/',
                                      {'name': 'name', 'description': 'nueva descripcion',
                                       'users': '1'},
                                      HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert workspace.status_code == 201