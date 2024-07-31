from django.test import TestCase
from django.utils import timezone
from .models import Task


class TaskModelTests(TestCase):

    def setUp(self):
        """
        Создаем задачу для тестов.
        """
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
        )

    def test_task_creation(self):
        """
        Тест получения задачи.
        """
        task = Task.objects.get(id=self.task.id)

        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test Description')
        self.assertEqual(task.status, Task.QUEUE)
        self.assertTrue(task.create_at <= timezone.now())

    def test_task_status_update(self):
        """
        Тест изменение задачи.
        """
        self.task.title = 'Update Task'
        self.task.description = 'Update Description'
        self.task.status = 'progress'
        self.task.save()

        task = Task.objects.get(id=self.task.id)

        self.assertEqual(task.title, 'Update Task')
        self.assertEqual(task.description, 'Update Description')
        self.assertEqual(task.status, Task.PROGRESS)

    def test_task_deletion(self):
        """
        Тест удаление задачи.
        """
        task_id = self.task.id

        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)
