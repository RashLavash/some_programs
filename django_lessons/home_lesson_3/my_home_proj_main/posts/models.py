from django.db import models
from django.db.models import CharField, TextField, DateTimeField, ForeignKey
from django.db.models import Model

from django.contrib.auth import get_user_model

User = get_user_model()


class Posts(Model):

    title = CharField(
        max_length=25,
        null=False,
        blank=False,
        help_text='Заголовок'
        )
    text = TextField(help_text='Текст')
    public_date = DateTimeField(
        auto_now_add = True,
        help_text='Дата создания публикации'
    )

    author = ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        help_text='Автор'
    )

    class Meta:
        ordering = ['-public_date']

