from celery import Celery, shared_task

app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')


@shared_task
def delete_expired_rows(self):
    print(1)
    print(f'Request: {self.request!r}')
