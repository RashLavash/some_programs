from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название марки')
    logo = models.ImageField(upload_to='brands/', blank=True, null=True, verbose_name='Логотип')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        ordering = ['name']

    def __str__(self):
        return self.name


class PriceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    max_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Максимальная цена')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Ценовая категория'
        verbose_name_plural = 'Ценовые категории'
        ordering = ['max_price']

    def __str__(self):
        return f"{self.name} (до {self.max_price} ₽)"


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('manual', 'Механика'),
        ('automatic', 'Автомат'),
        ('robot', 'Робот'),
        ('variator', 'Вариатор'),
    ]

    DRIVE_CHOICES = [
        ('front', 'Передний'),
        ('rear', 'Задний'),
        ('all', 'Полный'),
    ]

    FUEL_CHOICES = [
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('hybrid', 'Гибрид'),
        ('electric', 'Электро'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Марка', related_name='cars')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.IntegerField(verbose_name='Год выпуска')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    engine_volume = models.FloatField(verbose_name='Объем двигателя', help_text='в литрах')
    engine_type = models.CharField(max_length=20, choices=FUEL_CHOICES, verbose_name='Тип двигателя')
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, verbose_name='Коробка передач')
    drive = models.CharField(max_length=20, choices=DRIVE_CHOICES, verbose_name='Привод')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    mileage = models.IntegerField(verbose_name='Пробег', help_text='в километрах')
    power = models.IntegerField(verbose_name='Мощность', help_text='в лошадиных силах')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(PriceCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ценовая категория')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})

    def get_first_image(self):
        return self.images.filter(is_primary=True).first() or self.images.first()

    def get_all_images(self):
        return self.images.all()


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images', verbose_name='Автомобиль')
    image = models.ImageField(upload_to='cars/', verbose_name='Изображение')
    is_primary = models.BooleanField(default=False, verbose_name='Основное изображение')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Изображение автомобиля'
        verbose_name_plural = 'Изображения автомобилей'

    def save(self, *args, **kwargs):
        if self.is_primary:
            # Сделать это изображение основным, убрав метку с других
            CarImage.objects.filter(car=self.car, is_primary=True).update(is_primary=False)
        elif not CarImage.objects.filter(car=self.car, is_primary=True).exists():
            # Если нет основного изображения, сделать это основным
            self.is_primary = True
        super().save(*args, **kwargs)
