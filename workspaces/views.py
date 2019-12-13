import os

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.generics import get_object_or_404
from django.template.loader import render_to_string, get_template
from core.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from projects.models import Project
from projects.serializers import ProjectSerializer
from workspaces.models import Workspace
from rest_framework.decorators import action
from rest_framework.response import Response

from workspaces.serializers import WorkspaceSerializer, CreateWorkspaceSerializer


class ProjecSerializer(object):
    pass


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
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateWorkspaceSerializer
        return WorkspaceSerializer

    @action(detail=True, methods=['GET', 'POST', 'DELETE'])
    def users(self, request, pk=None):
        workspace = self.get_object()
        if request.method == 'GET':
            users = workspace.users.all()
            serialized = UserSerializer(users, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        elif request.method == 'POST':
            id = request.data.getlist('id')
            if id:
                for id in id:
                    user = get_object_or_404(User, id=id)
                    workspace.users.add(user)
                    rendered = render_to_string('userworkspace.html', {'name': user.first_name,
                                                                       'last_name': user.last_name,
                                                                       'workspace': workspace.name
                                                                       })
                    send_mail(
                        subject='Eres parte de {0}'.format(workspace.name),
                        html_message='{0}'.format(rendered),
                        message='',
                        from_email='Acamdelo@example.com',
                        recipient_list=['{0}'.format(user.email)],
                        fail_silently=False,
                    )

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            id = request.data.get('id', None)
            if id:
                user = get_object_or_404(User, id=id)
                workspace.users.remove(user)
                return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET', 'DELETE', 'POST'])
    def projects(self, request, pk=None):
        workspace = self.get_object()
        project = Project.objects.filter(workspace__id=workspace.id)
        serialized = ProjectSerializer(project, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

