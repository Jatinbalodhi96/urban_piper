from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=10)
    created_by = models.IntegerField()
    creation_date = models.DateTimeField('date published')