import os
from datetime import date, timedelta

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

import django
django.setup()
from pasteBin.models import Paste

app = Celery('PasteBin')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(86400.0, delete_expired_rows, name='removes expired rows')


@app.task
def delete_expired_rows():
    yesterday = date.today() - timedelta(days=1)
    Paste.objects.filter(expiration_date__lte=yesterday).delete()

    print('Removed!')
