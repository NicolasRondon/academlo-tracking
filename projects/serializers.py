from rest_framework import serializers

from core.serializers import UserSerializer
from workspaces.models import Workspace
from workspaces.serializers import WorkspaceSerializer
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    workspace = WorkspaceSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'users', 'workspace', 'created_at')


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'workspace', 'users', 'created_at')
