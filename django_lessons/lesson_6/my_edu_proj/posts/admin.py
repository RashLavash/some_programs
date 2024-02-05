from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # Настройка полей списка записей - какие поля будут отображаться и их порядок
    list_display = ['text', 'title', 'pub_date']
    # Сотрировка по дате
    list_filter = ['pub_date']
    # Поиск по названию полей
    search_fields = ['title', 'text']
    # Значение по умолочанию для пустого поля
    # empty_value_display = '-пусто-'
    # @admin.display(empty_value='-пусто-')
    # def text(self, objects):
    #     return objects.text

    # Исключение полей - исключаются в самом объекте
    # exclude = ['id', 'title']

    fieldsets = (
        ('Главные поля', {
            'fields': ('title',)
        }),
        ('Вторичные поля', {
            'fields': ('text', 'author')
        })
    )

admin.site.register(Post, PostAdmin)
