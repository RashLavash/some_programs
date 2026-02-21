#!/usr/bin/env python3
"""
Тестовый скрипт для проверки создания заказа
"""
import os
import sys
import django

# Добавляем путь к проекту
sys.path.append('/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avto_sales.settings')

# Инициализируем Django
django.setup()

from orders.models import Order
from cars.models import Car


def test_order_creation():
    """Тест создания заказа"""
    print("=== Тест создания заказа ===")
    
    # Проверяем наличие автомобилей
    cars_count = Car.objects.count()
    print(f"Количество автомобилей в базе: {cars_count}")
    
    if cars_count == 0:
        print("❌ Нет автомобилей для тестирования")
        return False
    
    # Берем первый автомобиль
    first_car = Car.objects.first()
    print(f"Тестируем с автомобилем: {first_car}")
    
    # Создаем заказ
    order_data = {
        'car': first_car,
        'full_name': 'Тестовый Пользователь',
        'phone': '+7 (999) 123-45-67',
        'total_amount': first_car.price,
        'status': 'new'
    }
    
    order = Order.objects.create(**order_data)
    print(f"✅ Заказ успешно создан: {order}")
    print(f"   ID: {order.id}")
    print(f"   Автомобиль: {order.car}")
    print(f"   Клиент: {order.full_name}")
    print(f"   Телефон: {order.phone}")
    print(f"   Сумма: {order.total_amount}")
    print(f"   Статус: {order.get_status_display()}")
    print(f"   Дата создания: {order.created_at}")
    
    # Проверяем, что заказ действительно сохранен
    saved_order = Order.objects.get(id=order.id)
    print(f"✅ Заказ найден в базе: {saved_order}")
    
    return True


def list_all_orders():
    """Вывод всех заказов"""
    print("\n=== Список всех заказов ===")
    
    orders = Order.objects.all().order_by('-created_at')
    
    if not orders:
        print("❌ Заказов нет в базе")
        return
    
    for order in orders:
        print(f"Заказ {order.id}:")
        print(f"  Автомобиль: {order.car}")
        print(f"  Клиент: {order.full_name}")
        print(f"  Телефон: {order.phone}")
        print(f"  Сумма: {order.total_amount}")
        print(f"  Статус: {order.get_status_display()}")
        print(f"  Дата: {order.created_at}")
        print()


if __name__ == '__main__':
    try:
        # Тестируем создание заказа
        test_order_creation()
        
        # Выводим все заказы
        list_all_orders()
        
    except Exception as e:
        print(f"❌ Ошибка при тестировании: {e}")
        import traceback
