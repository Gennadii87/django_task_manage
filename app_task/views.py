from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        """
        Получить список всех задач.
        """
        tasks = self.queryset
        context = {'request': request}
        serializer = self.serializer_class(tasks, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить конкретную задачу по ID.
        """
        try:
            pk = kwargs.get('pk')
            context = {'request': request}
            task = self.queryset.get(pk=pk)
            serializer = self.serializer_class(task, context=context)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        """
        Создать новую задачу.
        """
        context = {'request': request}
        serializer = self.serializer_class(data=request.data,  context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить задачу по ID.
        """
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

    def destroy(self, request, *args, **kwargs):
        """
        Удалить задачу по ID.
        """
        try:
            pk = kwargs.get('pk')
            task = self.queryset.get(pk=pk)
            task.delete()
            return Response({"deleted": task.title}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)
