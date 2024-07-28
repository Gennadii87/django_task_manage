from .models import Task

from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail', lookup_field='pk', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'create_at', 'url')

