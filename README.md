# django_task_manage
Task management system/Система управления задачами

![swagger](/image/swagger.png)
<br>

Swagger http://127.0.0.1:8000/swagger-ui/

<h2>Запуск в ручную</h2>

***Перед запуском в ручную необходимо установить и настроить RabbitMQ и ElasticSearch, рекомендуется использовать Docker***

Команды ручного запуска:

***Перед этим раскомментируйте в настройках Django код***

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

<h1>Запуск через Docker</h1>

Для сборки контейнеров запускаем 
    
    docker compose up -d

Для остановки 

    docker compose down

С удалением томов (рекомендуется) 
    
    docker compose down -v

***Внимание: если не получается скачивать образы то нужно использовать VPN***

Функционал:
<pre>

    - Создание, получение, редактирование и удаление задач
    - Сервис RabbitMQ и Celery для создания очереди задач | Rabbit - http://localhost:15672/#/ пароль и логин - guest
    - Сервис Flower для просмотра выполнения очереди задач http://localhost:5555/
    - Документация Swagger доступна http://127.0.0.1:8000/swagger-ui/
    - Полнотекстовый поиск задач через ElasticSearch по названию, описанию и статусу (http://localhost:9200/)

</pre>

Скриншоты программы:

![swagger](/image/swagger1.png)
<br>

![swagger](/image/swagger2.png)
<br>

![rabbit](/image/rabbit.png)
<br>

![flower](/image/flower.png)
<br>