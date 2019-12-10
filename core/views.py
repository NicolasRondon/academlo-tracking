from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status

from workspaces.models import Workspace
from workspaces.serializers import WorkspaceSerializer
from .serializers import UserSerializer, CreateUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa la instancia  de un usuario
    create:
        Crea un nuevo usuario
    list:
        Regresa la lista de Usuario
    update:
        Actualiza un usuario
    partial_update:
        Actualiza un campo en particular de un usuario
    delete:
        Elimina un usuario
    students:
        Regresa la lista de estudiantes
    isadmin:
        Regresa la lista de administradores
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer

    @action(detail=False, methods=['GET'])
    def students(self, request):
        students = User.objects.all().filter(is_staff=False)
        serialized = UserSerializer(students, many=True)
        if not students:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'There are not students'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=False, methods=['GET'])
    def isadmin(self, request):
        admin = User.objects.all().filter(is_staff=True)
        serialized = UserSerializer(admin, many=True)
        if not admin:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'There are not admins'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)


