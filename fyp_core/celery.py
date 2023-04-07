from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fyp_core.settings')
app = Celery('fyp_core')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "runs-every-30-seconds": {
        "task": "ticket_resolution.task.classify",
        "schedule": timedelta(seconds=30),
    },
    # executes every 1 minute
    # 'classify-task-one-min': {
    #     'task': 'ticket_resolution.tasks.classify',
    #     'schedule': crontab(),
    # },
    #executes every 15 minutes
    # 'scraping-task-fifteen-min': {
    #     'task': 'tasks.hackernews_rss',
    #     'schedule': crontab(minute='*/15')
    # },
}