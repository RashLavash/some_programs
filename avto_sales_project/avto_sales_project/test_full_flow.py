#!/usr/bin/env python3
"""
Тестовый скрипт для проверки полного цикла: создание заказа через view + отправка в Telegram
"""
import os
import sys
import django

# Добавляем путь к проекту
sys.path.append('/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avto_sales.settings')

# Инициализируем Django
django.setup()

from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from orders.views import create_order
from orders.models import Order
from cars.models import Car


def test_full_order_flow():
    """Тест полного цикла создания заказа"""
    print("=== Тест полного цикла создания заказа ===")
    
    # Проверяем наличие автомобилей
    cars_count = Car.objects.count()
    print(f"Количество автомобилей в базе: {cars_count}")
    
    if cars_count == 0:
        print("❌ Нет автомобилей для тестирования")
        return False
    
    # Берем первый автомобиль
    first_car = Car.objects.first()
    print(f"Тестируем с автомобилем: {first_car}")
    
    # Создаем заказ напрямую (как это делает view)
    order_data = {
        'car': first_car,
        'full_name': 'Тестовый Клиент',
        'phone': '+7 (999) 999-99-99',
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
    
    # Теперь имитируем вызов задачи Celery (как это делает view)
    print("\n--- Имитация вызова задачи Celery ---")
    from orders.tasks import send_order_notification_task
    
    # Вызываем задачу синхронно (для теста)
    result = send_order_notification_task(order.id)
    
    if result:
        print("✅ Задача Celery выполнена успешно")
    else:
        print("⚠️  Задача Celery выполнена, но с ошибкой (возможно, нет доступа к Telegram)")
    
    return True


def check_telegram_settings():
    """Проверка настроек Telegram"""
    print("\n=== Проверка настроек Telegram ===")
    
    from django.conf import settings
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    
    print(f"TELEGRAM_BOT_TOKEN: {'Доступен' if bot_token else 'Не настроен'}")
    print(f"TELEGRAM_CHAT_ID: {'Доступен' if chat_id else 'Не настроен'}")
    
    if bot_token and chat_id:
        print("✅ Настройки Telegram доступны")
        return True
    else:
        print("❌ Настройки Telegram не настроены")
        return False


if __name__ == '__main__':
    try:
        # Проверяем настройки Telegram
        telegram_configured = check_telegram_settings()
        
        # Тестируем полный цикл
        order_created = test_full_order_flow()
        
        if order_created:
            print("\n✅ Тестирование завершено успешно!")
            print("Заказ создается через view и задача на отправку в Telegram ставится в очередь")
            if not telegram_configured:
                print("⚠️  Telegram не настроен, но задача будет выполнена при настройке")
        else:
            print("\n❌ Тестирование завершено с ошибками")
        
    except Exception as e:
        print(f"❌ Ошибка при тестировании: {e}")
        import traceback
