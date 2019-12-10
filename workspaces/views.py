from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.generics import get_object_or_404

from core.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from workspaces.models import Workspace
from rest_framework.decorators import action
from rest_framework.response import Response

from workspaces.serializers import WorkspaceSerializer, CreateWorkspaceSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa la instancia  de un workspaces
    create:
        Crea un nuevo workspace
    list:
        Regresa la lista de workspaces
    update:
        Actualiza un workspace
    partial_update:
        Actualiza un campo en particular de un workspace
    delete:
        Elimina un workspace
    """
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'tags']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateWorkspaceSerializer
        return WorkspaceSerializer

    @action(detail=True, methods=['GET'])
    def students(self, request, pk=None):
        """
        Regresa la lista de estudiantes de un workspace
        """
        workspace = self.get_object()
        users = workspace.users.filter(is_staff=False)
        serialized = UserSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def admin(self, request, pk=None):
        """
        Regresa la lista de administradores que pertenecen a un workspace
        """
        workspace = self.get_object()
        users = workspace.users.filter(is_staff=True)
        serialized = UserSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def users(self, request, pk=None):
        workspace = self.get_object()
        users = workspace.users.all()
        serialized = UserSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET', 'POST', 'DELETE'])
    def invite(self, request, pk=None):
        workspace = self.get_object()
        if request.method == 'GET':
            users = workspace.users.all()
            serialized = UserSerializer(users, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        elif request.method == 'POST':
            id = request.data.get('id', None)
            if id:
                #user = User.objects.get(id=id)
                user = get_object_or_404(User, id=id)
                workspace.users.add(user)
                send_mail(
                    subject='Hola {0}, ahora formas parte de {1}'.format(user.first_name, workspace.name),
                    message='Este año haremos tal y tal cosa',
                    from_email='from@example.com',
                    recipient_list=['{0}'.format(user.email)],
                    fail_silently=False,
                          )
                return Response(status=status.HTTP_200_OK)
        else:
            id = request.data.get('id', None)
            if id:
                # user = User.objects.get(id=id)
                user = get_object_or_404(User, id=id)
                workspace.users.remove(user)
                return Response(status=status.HTTP_200_OK)