from rest_framework import serializers
from .models import Post

from datetime import datetime

# 1 class Serializer
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     text = serializers.CharField()
#     pub_date = serializers.DateTimeField(read_only=True)


#     def create(self, validated_data):

#         return Post.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)

#         return instance


# 2 class ModelSerializer

class PostSerializer(serializers.ModelSerializer):
    
    post_title = serializers.CharField(source='title')

    # Из словаря в json (к примеру)
    def to_representation(self, instance):
        # return super().to_representation(instance)
        representation = super().to_representation(instance)

        representation['pub_date'] = instance.pub_date.strftime('%d %m %Y')

        return representation
    
    # Из словаря в объект

    def to_internal_value(self, data):
        data['pub_date'] = datetime.strptime(data['pub_date'], '%d %m %Y').date()


        return super().to_internal_value(data)


    class Meta:
        model = Post
        fields = ('post_title', 'text', 'pub_date')
        # fields = '__all__'

