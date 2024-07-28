# Generated by Django 4.2 on 2024-07-28 22:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='название задачи', max_length=128, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(128)], verbose_name='название')),
                ('description', models.CharField(help_text='описание задачи', max_length=512, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(512)], verbose_name='описание')),
                ('status', models.CharField(choices=[('queue', 'в очереди'), ('progress', 'в процессе'), ('completed', 'завершена')], default='queue', help_text='статус задачи', verbose_name='статус')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='дата создания задачи', verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
    ]
