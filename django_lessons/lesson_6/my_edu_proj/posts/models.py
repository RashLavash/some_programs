from django.db import models
from django.contrib.auth import get_user_model


RATING = [(1, 'Плохо'), (2, 'Посредственно'), (3, 'Нормально'), (4, 'Хорошеечно')]

User = get_user_model()


class Post(models.Model):
    # IntegerField, FloatField, EmailField, Filefield, ImageField
    title = models.CharField(max_length=100)
    text = models.TextField(help_text='Текст', null=False, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
        )
    
    def __str__(self):
        # return f'{self.title[:30]}' # Длина макс 30 символов
        # return self.title[:30] # Длина макс 30 символов
        return self.title # Длина макс 30 символов

