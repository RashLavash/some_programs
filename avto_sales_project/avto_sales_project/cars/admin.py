from django.contrib import admin
from .models import Brand, PriceCategory, Car, CarImage


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1
    fields = ['image', 'is_primary']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'max_price']
    list_filter = ['max_price']
    search_fields = ['name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'engine_type', 'transmission', 'is_active', 'created_at']
    list_filter = ['brand', 'engine_type', 'transmission', 'drive', 'is_active', 'created_at']
    search_fields = ['brand__name', 'model', 'year']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [CarImageInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('brand', 'model', 'year', 'price', 'category')
        }),
        ('Технические характеристики', {
            'fields': ('engine_type', 'engine_volume', 'power', 'transmission', 'drive', 'color', 'mileage')
        }),
        ('Описание', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
        ('Статус', {
            'fields': ('is_active', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ['car', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    raw_id_fields = ['car']
