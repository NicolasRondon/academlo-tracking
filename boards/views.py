from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.permissions import AllowAny, IsAdminUser

from boards.models import Board
from boards.serializers import BoardSerializer, CreateBoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBoardSerializer
        return BoardSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]

        return [permission() for permission in self.permission_classes]