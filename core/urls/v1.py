from django.urls import path, include
from rest_framework import routers

from boards.views import BoardViewSet
from core.views import UserViewSet
from projects.views import ProjectViewSet
from tasks.views import TaskViewSet
from workspaces.views import WorkspaceViewSet
from comments.views import CommentViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'workspace', WorkspaceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]