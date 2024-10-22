from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task


@extend_schema(tags=["Tasks"])
class TaskViewSet(viewsets.ViewSet):
    queryset = Task.objects.order_by('id')
    serializer_class = TaskSerializer

    @extend_schema(summary='Получить список задач')
    def list(self, request, *args, **kwargs):

        tasks = self.queryset.all()
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Получить задачу по id')
    def retrieve(self, request, *args, **kwargs):

        try:
            pk = kwargs.get('pk')
            task = self.queryset.get(pk=pk)
            serializer = self.serializer_class(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(summary='Создать новую задачу')
    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            process_task.delay(task.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary='Изменить задачу')
    def partial_update(self, request, *args, **kwargs):

        try:
            pk = kwargs.get('pk')
            task = self.queryset.get(pk=pk)

            serializer = self.serializer_class(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(summary='Удалить задачу')
    def destroy(self, request, *args, **kwargs):

        try:
            pk = kwargs.get('pk')
            task = self.queryset.get(pk=pk)
            task.delete()
            return Response({"deleted": task.title}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)
