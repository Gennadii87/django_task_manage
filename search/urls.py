from django.urls import path

from search.views import SearchTask

urlpatterns = [
    path('task/<str:query>/', SearchTask.as_view()),
    path('task/all/', SearchTask.as_view(), name='all_tasks'),
]
