from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter


from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer
from .models import Post
from .filters import CustomFilter


User = get_user_model()


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title','author']
    # filter_backends = [SearchFilter]
    # search_fields = ['title', 'text']
    
    # ^, =, $, 
    search_fields = ['title', 'author__username']

    # OrderingFilter
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'text']
    ordering = ['text']

    # def get_queryset(self):
    #     # user = self.request.user
    #     # user_id = self.kwargs.get('id')
    #     user_id = self.request.query_params.get('id')
    #     user = User.objects.get(pk=user_id)

    #     return Post.objects.filter(author=user)