from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer


@api_view(['GET', 'POST'])
def index(request):

    '''
    Главная страница
    '''

    if request.method == 'POST':

        return Response({"message": "Данные получены", "data": request.data})
    
    return Response({"message": "Главная страница"})


@api_view(['GET', 'POST'])
def post_list(request):

    '''
    Получаем список публикаций, либо создаем новую
    '''
    
    if request.method == 'GET':

        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(author=request.user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':

        serializer = PostSerializer(post)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT' or request.method == 'PATCH':

        serializer = PostSerializer(post, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':

        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





