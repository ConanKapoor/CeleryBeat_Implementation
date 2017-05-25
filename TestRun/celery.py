from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta
from testing.tasks import *
from testing.views import *

app = Celery('TestRun')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestRun.settings')

app.conf.beat_schedule = {
    'nslookup-every-10-seconds': {
        'task': 'testing.tasks.nslookup',
        'schedule': timedelta(seconds=10),
        'args': (web_url,),
    },
    'nmap-every-10-seconds': {
        'task': 'testing.tasks.nmap',
        'schedule': timedelta(seconds=10),
        'args': (web_url,),
    },
}
app.conf.timezone = 'UTC'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
