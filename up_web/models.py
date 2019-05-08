from django.db import models
from datetime import datetime

class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    priority = models.CharField(max_length=10)
    created_by = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=datetime.now, blank=True)