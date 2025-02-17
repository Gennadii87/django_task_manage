 ![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FFFFF?style=for-the-badge&logo=rabbitmq&logoColor=FF6600)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)![Celery](https://img.shields.io/badge/Celery-ff1709?style=for-the-badge&logo=celery&logoColor=white)![elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
# django_task_manage
Task management system/Система управления задачами

![swagger](/image/swagger.png)
<br>

Swagger http://127.0.0.1:8000/swagger-ui/

### Запуск в ручную

***Перед запуском в ручную необходимо установить и настроить PostgreSQL, RabbitMQ и ElasticSearch, рекомендуется использовать Docker***

Команды ручного запуска, например на Windows:

Создайте файл `.env` и внесите туда данные из примера, или укажите свои <br/>
Разместите его в корне проекта там где файл `manage.py` <br/>
Создайте базу данных в PostgreSQL <br/> 

Пример файла `.env`
<pre>
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=superuser
    POSTGRES_DB=tasks_db
    HOST=localhost
    PORT=5432

    ELASTIC_HOST='http://localhost:9200'
    CELERY_BROKER_URL = 'pyamqp://guest:guest@localhost//'
</pre>

***Убедитесь что  PostgreSQL, RabbitMQ и Elasticsearch  настроены и работают***

Обновить менеджер pip:
    
    python -m pip install --upgrade pip

Выполнить миграции:

    python manage.py migrate 

Запуск Celery для Windows:
    
    celery -A main worker -l INFO --pool solo

Запуск Flower:

     celery -A main flower  

Чтобы создать и заполнить индекс и сопоставление Elasticsearch, используйте команду search_index:
    
    python manage.py search_index --rebuild 

Выполнить запуск приложения:

    python manage.py runserver  

### Запуск через Docker

Если запускать через Docker, то `.env` создавать не нужно, все необходимое есть в `.env_docker`

Для сборки контейнеров запускаем 
    
    docker compose up -d

Для остановки 

    docker compose down

С удалением томов (рекомендуется) 
    
    docker compose down -v

***ВАЖНО! Если не получается скачивать образы, то нужно использовать VPN или proxy***

### Функционал:
<pre>
    - Создание, получение, редактирование и удаление задач
    - Сервис RabbitMQ и Celery для создания очереди задач 
    - Сервис Flower для просмотра выполнения очереди задач 
    - Документация api типа Swagger 
    - Полнотекстовый поиск задач через Elasticsearch  по названию, описанию и статусу
    - Полнотекстовый поиск задач через используя API  по названию, описанию и статусу
</pre>
### Запуск тестов

    python manage.py test -v 2

### Наполнение тестовыми данными
Сервис можно наполнить тестовыми данными загрузив фикстуру:
    
     python manage.py loaddata fixture.json

***ВАЖНО! Загрузка фикстуры должна проводиться после запуска сервиса и заполнения индекса и сопоставление Elasticsearch***

### Таблица сервисов

| Сервис        | хост                          | Описание функций                                                                   |
|---------------|-------------------------------|------------------------------------------------------------------------------------|
| API (task)    | http://127.0.0.1:8000/task/   | Управление задачами: создание, чтение, обновление, удаление                        |
| Api (search)  | http://127.0.0.1:8000/search/ | all/ - поиск всех задач, {query}/ поиск по параметрам (название, описание, статус) |
| Flower        | http://localhost:5555         | Мониторинг состояния задач и активности воркеров                                   |
| Elasticsearch | http://localhost:9200         | Поиск всех задач /tasks/_search?pretty, с параметрами /tasks/_search?q=поле:слово  |
| RabbitMQ      | http://localhost:15672        | Админ панель и дашборд login: guest password: guest                                |

Скриншоты сервисов:

![swagger](/image/swagger1.png)
<br>

![swagger](/image/swagger2.png)
<br>

![rabbit](/image/rabbit.png)
<br>

![flower](/image/flower.png)
<br>
