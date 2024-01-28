from django.db import models
from django.contrib.auth import get_user_model


RATING = [(1, 'Плохо'), (2, 'Посредственно'), (3, 'Нормально'), (4, 'Хорошеечно')]

User = get_user_model()


class Post(models.Model):
    # IntegerField, FloatField, EmailField, Filefield, ImageField
    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, # SET_NULL, SET_DEFAULT, PROTECT
        related_name='posts'
        )
    
    class Meta:
        ordering = ['-pub_date']


class Review(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(choices=RATING)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=False,
        null=False,
    )
    comments = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)