from .models import Task
from celery import shared_task
import time


@shared_task
def process_task(task_id):
    """Имитация выполнения задачи"""
    time.sleep(10)
    task = Task.objects.get(id=task_id)
    task.status = Task.COMPLETED
    task.save()
