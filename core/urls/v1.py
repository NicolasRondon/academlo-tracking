from django.urls import path, include
from rest_framework import routers
from core.views import UserViewSet
from workspaces.views import WorkspaceViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'workspace', WorkspaceViewSet)

urlpatterns = [
    path('', include(router.urls))
]