from .models import Task

from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'create_at')
