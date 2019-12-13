from rest_framework import serializers

from core.serializers import UserSerializer
from .models import Task
from boards.serializers import BoardSerializer


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    board = BoardSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'user', 'board', 'name', 'description', 'due_date', 'position', 'created_at')


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('user', 'board', 'name', 'description', 'due_date', 'position', 'created_at')
