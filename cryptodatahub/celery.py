import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptodatahub.settings')

app = Celery('cryptodatahub')

# Load tasks from installed Django apps
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'fetch_crypto_prices_every_5_min': {
        'task': 'myapp.task.fetch_crypto_prices',
        'schedule': crontab(minute='*/5'),  # Every 5 minutes
    },
}