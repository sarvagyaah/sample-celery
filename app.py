import os
from celery import Celery
R_HOST = os.getenv('REDIS_HOST')
R_PORT =  os.getenv('REDIS_PORT')
redis_url = f'redis://{R_HOST}:{R_PORT}/0'

celery_app = Celery(
    'worker',
    broker = redis_url,
    backend = redis_url
)
@celery_app.task(name="tasks.add")
def add():
    return 5