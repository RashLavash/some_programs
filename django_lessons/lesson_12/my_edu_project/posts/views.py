from rest_framework import generics

from .serializer import PostSerializer, CategorySerializer
from .models import Post, Category


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()

    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()

    serializer_class = PostSerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer
