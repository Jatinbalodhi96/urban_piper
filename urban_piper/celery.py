from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, shared_task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urban_piper.settings')

app = Celery('urban_piper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# @app.task()
# def debug_task(self):
#     return 'string'

@app.task
def add(self, x, y):
    return x + y
