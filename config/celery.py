import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery beat

app.conf.beat_schedule = {
    'periodic-mailing': {
        'task': 'main.tasks.periodic_send',
        'schedle': crontab(minute='*/5'),
    },
}