from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=300, default='Nuevo espacio de trabajo')
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
