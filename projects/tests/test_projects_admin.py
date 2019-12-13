from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class ProjectTestCases(APITestCase):
    def setUp(self):
        self.usser = User.objects.create_superuser('test_admin', 'admin@admin.com', '123456')

    def test_admin_project_get(self):
        result = self.client.post('/api/token/', {'username': 'test_admin', 'password': '123456'})
        token = result.data['access']
        projects = self.client.get('/api/v1/projects/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert projects.status_code == 200

    def test_admin_project_post(self):
        result = self.client.post('/api/token/', {'username': 'test_admin', 'password': '123456'})
        token = result.data['access']
        project = self.client.post('/api/v1/projects/',
                                   {'name': 'name', 'description': 'decripcion', 'workspace': '1'},
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert project.status_code == 400
