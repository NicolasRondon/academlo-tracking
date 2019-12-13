from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from boards.models import Board


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=450)
    due_date = models.DateField()
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
