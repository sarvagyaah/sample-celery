import os
from celery import Celery
redis_url = f'redis://{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}/0'

celery_app = Celery(
    'worker',
    broker = redis_url,
    backend = redis_url
)
@celery_app.task(name="tasks.add")
def add():
    return 5