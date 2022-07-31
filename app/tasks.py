import time

import requests
from . import celery_app
from .models import Device


@celery_app.task(name="create_task")
def create_task(device_id: Device):
    time.sleep(2.0)
    request_data = requests.get(
        f'https://localhost:8001/devices/{device_id}'
    )                                       # requesting data from external microservice (FastAPI)
    return request_data
