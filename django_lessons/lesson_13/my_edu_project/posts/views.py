from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer



@api_view(['GET', 'POST'])
def index(request):

    '''
    Главная страница.
    '''
    
    if request.method == 'POST':
        return Response({'message': 'Получены данные', 'data': request.data})
    
    return Response({'message': 'Главная страница'})


# @api_view(['GET', 'POST'])
# def post_list(request):
#     '''
#     Получаем список публикаций либо создаем новую запись
#     '''

#     if request.method == 'GET':
#         posts = Post.objects.all()

#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save(author=request.user)

#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def post_detail(request, pk):
#     '''
#     Получаем, изменяем или удаляем отдельную публикацию
#     '''

#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'GET':

#         serializer = PostSerializer(post)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'PUT' or request.method == 'PUTCH':

#         serializer = PostSerializer(post, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':

#         post.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)




# class APIPostList(APIView):
#     '''
#     Получаем список публикаций либо создаем новую запись
#     '''

#     def get(self, request):
#         posts = Post.objects.all()

#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save(author=request.user)

#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class APIPostDetail(APIView):
#     '''
#     Получаем, изменяем или удаляем отдельную публикацию
#     '''

#     def get(self, request, pk=None):

#         post = get_object_or_404(Post, pk=pk)

#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def put(self, request, pk=None):

#         post = get_object_or_404(Post, pk=pk)

#         serializer = PostSerializer(post, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def patch(self, request, pk=None):

#         post = get_object_or_404(Post, pk=pk)

#         serializer = PostSerializer(post, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk=None):

#         post = get_object_or_404(Post, pk=pk)

#         post.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)


class PostList(generics.ListCreateAPIView):
    '''
    Получаем список публикаций либо создаем новую запись
    '''

    queryset = Post.objects.all()
    serializer_class = PostSerializer 
     

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Получаем, изменяем или удаляем отдельную публикацию
    '''

    queryset = Post.objects.all()
    serializer_class = PostSerializer

