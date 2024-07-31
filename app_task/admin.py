from django.contrib import admin
from app_task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at')
    fields = ('title', 'description', 'status', 'create_at')
    readonly_fields = ('create_at',)


admin.site.register(Task, TaskAdmin)
