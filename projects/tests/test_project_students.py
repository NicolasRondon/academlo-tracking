from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class ProjectTestCases(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user', 'user@ada.com', '123456')

    def test_project_student_get(self):
        result = self.client.post('/api/token/', {'username':'test_user', 'password':'123456'})
        token = result.data['access']
        projects = self.client.get('/api/v1/projects/', HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert projects.status_code == 200

    def test_project_student_get(self):
        result = self.client.post('/api/token/', {'username': 'test_user', 'password': '123456'})
        token = result.data['access']
        project = self.client.post('/api/v1/projects/',
                                   {'name': 'name', 'description': 'descripcion', 'worksapce': '1'},
                                   HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        assert project.status_code == 403