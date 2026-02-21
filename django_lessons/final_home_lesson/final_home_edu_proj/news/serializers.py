from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):

    '''
    Сериалайзер для модели News
    '''

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = News
        fields = ('title', 'text', 'pub_date', 'author')

