from django.contrib.auth.models import User
from django.db import models
from workspaces.models import Workspace
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Project(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name