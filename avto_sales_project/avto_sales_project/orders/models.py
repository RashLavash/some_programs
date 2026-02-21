from django.db import models
from django.contrib.auth.models import User
from cars.models import Car


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('confirmed', 'Подтвержден'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль', related_name='orders')
    full_name = models.CharField(max_length=200, verbose_name='ФИО клиента')
    phone = models.CharField(max_length=20, verbose_name='Контактный телефон')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итоговая сумма')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ {self.id} на {self.car} от {self.full_name}"
