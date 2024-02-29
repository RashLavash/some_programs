from django.utils import timezone

from rest_framework import serializers
from .models import Post, Category


class BigName(serializers.Field):
    def to_representation(self, value):
        return (value.upper())
    
    def to_internal_value(self, data):
        data = data[0] + data[1:].lower()
        return data


class PostSerializer(serializers.ModelSerializer):
    # По умолчанию стоит поле serializer.PrymaryKeyRelatedField
    # Можно заменить на  serializer.StringRelatedField, serializer.SlugRelatedField, 
    # serializer.HyperlinkedRelatedField и т.д.
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField()

    # Задаем полю title созданный тип BigName
    title = BigName()


    def validate(self, attrs):
        if attrs['pub_date'] < attrs['create_date']:
            raise serializers.ValidationError(
                'Публдикация не может быть опубликована раньше ее создания.'
            )
        return attrs


    def validate_pub_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'Публикация статьи не может произойти в прошлом.'
            )
        return value    

    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'author', 'category')


    

class CategorySerializer(serializers.ModelSerializer):

    posts = serializers.StringRelatedField(read_only=True, many=True)
    posts = PostSerializer(read_only=True, many=True)

    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('title', 'posts', 'count')

    def get_count(self, obj):
        return obj.posts.count()
