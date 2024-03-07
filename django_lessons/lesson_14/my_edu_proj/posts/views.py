from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import GenericViewSet

from rest_framework import mixins

from rest_framework.response import Response

from rest_framework.decorators import action

from .models import Post
from .serializers import PostSerializer, PostListSerializer


class PostViewSet(ModelViewSet):

    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

    @action(detail=False, methods=['get'])
    def last_updated(self, request):
        post = Post.objects.last()

        serializer = PostSerializer(post)

        return Response(serializer.data)
    

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        
        return PostSerializer
    

    def get_queryset(self):
        new_set = Post.objects.filter(pub_date__month__gte=3)
        return new_set


# class PostViewSet(ReadOnlyModelViewSet):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class BasePostViewSet(ViewSet):
    def list(self, request):
        posts = Post.objects.all()

        serializer = PostListSerializer(posts, many=True)

        return Response(serializer.data)

    
    def create(self, request):
        pass


    def retrieve(self, request, pk=None):
        pass


    def update(self, request, pk=None):
        pass


    def partial_update(self, request, pk=None):
        pass


    def destroy(self, request, pk=None):
        pass


class ListCreateRetrieveUpdateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet):


    queryset = Post.objects.all()
    serializer_class = PostSerializer


