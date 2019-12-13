from django.db import models

# Create your models here.
from projects.models import Project


class Board(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    position = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.position:
            self.position = Board.objects.all().count() + 1
        super(Board, self).save(*args, **kwargs)