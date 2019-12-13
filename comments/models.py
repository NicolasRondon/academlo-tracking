from django.contrib.auth.models import User
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
# Create your models here.
from tasks.models import Task


class Comment(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id