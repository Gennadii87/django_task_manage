# django_task_manage
Task management system/Система управления задачами

Обновить менеджер pip:
    
    python -m pip install --upgrade pip

Выполнить миграции:

    python manage.py migrate 

Запуск Celery для Windows:
    
    celery -A main worker -l INFO --pool solo

Запуск Flower:

     celery -A main flower  

Выполнить индексацию для ElasticSearch:
    
    python manage.py search_index --rebuild 

Выполнить запуск приложения:

    python manage.py runserver  


Для сборки контецнеров запускаем docker compose up -d

для остановки docker compose down

с удалением томов (рекомендуется) docker compose down -v