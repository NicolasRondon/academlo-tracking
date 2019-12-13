from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import ProjectSerializer, CreateProjectSerializer
from .models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa la instancia de proyectos
    create:
        Crea un nuevo proyecto
    list:
        Regresa la lista de proyectos
    update:
        Actualiza un proyecto
    partial_update:
        Actualiza un campo en particular de un proyecto
    delete:
        Elimina un proyecto
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProjectSerializer
        return ProjectSerializer
