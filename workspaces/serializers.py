from rest_framework import serializers

from core.serializers import UserSerializer
from .models import Workspace
from django.core.mail import send_mail


class WorkspaceSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ('id', 'name', 'description', 'users', 'created_at',)


class CreateWorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('name', 'description', 'users', 'created_at',)


class UsersWorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('users',)
