from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from app_task.models import Task


@registry.register_document
class CategoryDocument(Document):
    id = fields.IntegerField()
    title = fields.TextField()
    description = fields.TextField()
    status = fields.TextField()

    class Index:
        name = 'tasks'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Task
        fields = [
            'create_at',
        ]
