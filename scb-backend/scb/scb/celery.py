import os
from pathlib import Path

from celery import Celery

from .settings import CONFIG

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scb.settings")
BASE_DIR = Path(__file__).resolve().parent.parent

app = Celery(
    "red",
    broker=(
        f"amqp://{CONFIG.rabbit_user}:{CONFIG.rabbit_password}@"
        f"{CONFIG.rabbit_host}:{CONFIG.rabbit_port}/"
    ),
    backend=(f"redis://{CONFIG.redis_host}:{CONFIG.redis_port}/{CONFIG.redis_db}"),
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
