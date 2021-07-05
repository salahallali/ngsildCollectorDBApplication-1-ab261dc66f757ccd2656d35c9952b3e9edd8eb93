from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Service(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    status = models.CharField(default='active', max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.id

