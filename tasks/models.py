from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from boards.models import Board
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Task(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=450)
    due_date = models.DateField()
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.position:
            self.position = Task.objects.all().count() + 1
        super(Task, self).save(*args, **kwargs)
