import abc

from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from .documents import TaskDocument
from app_task.serializers import TaskSerializer


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden and return a Q() expression."""
        pass

    def get(self, request, query=None):
        try:
            if query:
                q = self.generate_q_expression(query)
                search = self.document_class.search().query(q)
            else:
                search = self.document_class.search()

            response = search.execute()
            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


@extend_schema(tags=["Search tasks"])
class SearchTask(PaginatedElasticSearchAPIView):
    serializer_class = TaskSerializer
    document_class = TaskDocument

    def generate_q_expression(self, query):
        return Q(
            'multi_match', query=query,
            fields=[
                'title',
                'description',
                'status',
            ], fuzziness='auto'
        )
