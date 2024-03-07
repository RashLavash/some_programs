# Paginations

# PageNumberPagination
# LimitOffsetPagination
# CursorPagination

from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response

from .serializers import PostSerializer


class PostPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


    def get_paginated_response(self, data):
        pagination_serializer = PostSerializer(data)
        return Response({
            'number': self.page.paginator.count,
            'data': data
        })
    
    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)
        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param)
        return paginator.page(page_number)


