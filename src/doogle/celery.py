from django.conf import settings
from celery import Celery


app = Celery('doogle')
app.config_from_object(settings.CELERY_CONFIGURATION)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
