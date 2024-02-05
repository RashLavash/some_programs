from django.db import models
from django.contrib.auth import get_user_model


RATING = [(1, 'Плохо'), (2, 'Посредственно'), (3, 'Нормально'), (4, 'Хорошеечно')]

User = get_user_model()



class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False)


class Post(models.Model):
    # IntegerField, FloatField, EmailField, Filefield, ImageField
    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        help_text='Заголовок',
        verbose_name='Заголовок публикации'
    )
    text = models.TextField(help_text='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, # SET_NULL, SET_DEFAULT, PROTECT
        related_name='posts',
        help_text='Автор',
        verbose_name='Автор публикации'
        )
    
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        through='PostTag',
        help_text='Теги',
        verbose_name='Теги публикации'
        )
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикация' # Убираем на конце слова лишнюю букву s

    def __str__(self):
        # return f'{self.title[:30]}' # Длина макс 30 символов
        # return self.title[:30] # Длина макс 30 символов
        return f'{self.title[:30]}' # Длина макс 30 символов


# Промежуточная таблица
class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Comments(models.Model):
    comments = models.TextField()

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
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # Зависимость Один-к-Одному
    comments = models.OneToOneField(
        Comments,
        on_delete=models.SET_NULL,
        null=True,
        related_name='review'
    )
