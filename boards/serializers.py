from rest_framework import serializers

from projects.serializers import ProjectSerializer
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'name', 'project', 'position', 'created_at')


class CreateBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('name', 'project', 'position', 'created_at')
