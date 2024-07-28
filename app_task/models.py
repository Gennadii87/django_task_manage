from django.db import models
from django.conf import settings as s
from django.core import validators as vl


class ValidatorTask:
    title_validator = [vl.MinLengthValidator(3), vl.MaxLengthValidator(128)]
    description_validator = [vl.MinLengthValidator(5), vl.MaxLengthValidator(512)]


class Task(models.Model):

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    QUEUE = 'в очереди'
    PROGRESS = 'в процессе'
    COMPLETED = 'завершена'

    STATUS_CHOICES = [
        (QUEUE, 'в очереди'),
        (PROGRESS, 'в процессе'),
        (COMPLETED, 'завершена'),
    ]

    title = models.CharField(
                            help_text='название задачи',
                            verbose_name='название',
                            max_length=128,
                            validators=ValidatorTask.title_validator
                            )
    description = models.CharField(
                            help_text='описание задачи',
                            verbose_name='описание',
                            max_length=512,
                            validators=ValidatorTask.description_validator
                           )
    status = models.CharField(choices=STATUS_CHOICES, blank=True, help_text='статус задачи', verbose_name='статус')
    create_at = models.DateTimeField(auto_now_add=True, help_text='дата создания задачи', verbose_name='дата создания')

    def __str__(self):
        return f"{self.title}  {self.status}  создана: {self.create_at.strftime('%d.%m.%Y - %X')}({s.TIME_ZONE})"
