from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'car', 'full_name', 'phone', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'phone', 'car__model']
    readonly_fields = ['created_at', 'updated_at']
    raw_id_fields = ['car']
    
    fieldsets = (
        ('Информация о заказе', {
            'fields': ('car', 'total_amount', 'status')
        }),
        ('Контактные данные', {
            'fields': ('full_name', 'phone')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
