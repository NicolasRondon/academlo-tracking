from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from workspaces.models import Workspace


class WorkspaceTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'test_user@mail.com', '123456')
        self.useradmin = User.objects.create_superuser('test_admin', 'admin@admin.com', '123456')

    def test_student_workspace_get(self):
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})
        token = result.data['access']
        workspaces = self.client.get('/api/v1/workspace/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert workspaces.status_code == 200

    def test_student_workspace_create(self):
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})
        token = result.data['access']
        workspace = self.client.post('/api/v1/workspace/',
                                      {'id': '1', 'name': 'name', 'description': 'nueva descripcion',
                                       'users': 'test_user'},
                                      HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert workspace.status_code == 403

    def test_student_workspace_delete(self):
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})
        token = result.data['access']
        workspace = self.client.delete('/api/v1/workspace/',
                                      {'id': '1', 'name': 'name', 'description': 'nueva descripcion',
                                       'users': 'test_user'},
                                      HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert workspace.status_code == 403