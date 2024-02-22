# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()

#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()

#     serializer_class = PostSerializer


class PostListAPIView(APIView):
    
    def get(self, request):
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        # serializer.initial_data - поулчаем данные до валидации
        if serializer.is_valid():
            serializer.save()
        # serializer.data - все данные, без ошибок, поучаем после сохранения 
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
