from django.db import models
from django.contrib.auth.models import User
from cars.models import Car


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автомобиль', related_name='reviews')
    full_name = models.CharField(max_length=200, verbose_name='Полное имя', null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Оценка')
    text = models.TextField(verbose_name='Текст отзыва')
    is_approved = models.BooleanField(default=False, verbose_name='Одобрен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name
