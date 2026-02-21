from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import News
from .serializers import NewsSerializer


@api_view(['GET'])
def index(request) -> Response:

    '''
    Получаем сообщение о главной странице
    '''

    return Response({'message': 'Главная страница'})


class NewsList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    
    queryset = News.objects.all()
    serializer_class = NewsSerializer


    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
    

class NewsDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    
    queryset = News.objects.all()
    serializer_class = NewsSerializer


    def get(self, request, *args, **kwargs):
        
        return self.retrieve(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        
        return self.update(request, *args, **kwargs)
    
    
    def patch(self, request, *args, **kwargs):
        
        return self.partial_update(request, *args, **kwargs)
    
    
    def delete(self, request, *args, **kwargs):
        
        return self.destroy(request, *args, **kwargs)
    

