from django.shortcuts import render

from tasks.models import Task
from .serializers import TaskSerializer, CreateTaskSerializer
from rest_framework import viewsets


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTaskSerializer
        return TaskSerializer
