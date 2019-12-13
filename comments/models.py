from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from tasks.models import Task


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id