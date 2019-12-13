from django.contrib.auth.models import User
from django.db import models
from workspaces.models import Workspace
from django.template.loader import render_to_string
from django.core.mail import send_mail


class Project(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        send_mail('Subject here', 'Here is the message.',
                  'from@example.com', ['nikolaasrondon@gmail.com'], fail_silently=False)
        super(Project, self).save(*args, **kwargs)
