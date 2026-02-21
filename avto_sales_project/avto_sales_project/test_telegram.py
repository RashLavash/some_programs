#!/usr/bin/env python3
"""
Тестовый скрипт для проверки отправки сообщений в Telegram
"""
import os
import sys
import django

# Добавляем путь к проекту
sys.path.append('/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avto_sales.settings')

# Инициализируем Django
django.setup()

from orders.tasks import send_order_notification_task
from orders.models import Order
from cars.models import Car


def test_telegram_notification():
    """Тест отправки уведомления в Telegram"""
    print("=== Тест отправки уведомления в Telegram ===")
    
    # Проверяем настройки
    from django.conf import settings
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    
    print(f"TELEGRAM_BOT_TOKEN: {'Доступен' if bot_token else 'Не настроен'}")
    print(f"TELEGRAM_CHAT_ID: {'Доступен' if chat_id else 'Не настроен'}")
    
    if not bot_token or not chat_id:
        print("❌ Telegram не настроен в settings.py")
        return False
    
    # Проверяем наличие заказов
    orders_count = Order.objects.count()
    print(f"Количество заказов в базе: {orders_count}")
    
    if orders_count == 0:
        print("❌ Нет заказов для тестирования")
        return False
    
    # Берем последний заказ
    latest_order = Order.objects.latest('created_at')
    print(f"Тестируем заказ: {latest_order}")
    
    # Тестируем отправку
    print("\n--- Тест отправки сообщения ---")
    result = send_order_notification_task(latest_order.id)
    
    if result:
        print("✅ Сообщение успешно отправлено в Telegram")
    else:
        print("❌ Ошибка отправки сообщения в Telegram")
    
    return result


def test_celery_task():
    """Тест асинхронной задачи Celery"""
    print("\n=== Тест асинхронной задачи Celery ===")
    
    from orders.models import Order
    
    orders_count = Order.objects.count()
    
    if orders_count == 0:
        print("❌ Нет заказов для тестирования")
        return False
    
    latest_order = Order.objects.latest('created_at')
    print(f"Тестируем асинхронную задачу для заказа: {latest_order}")
    
    # Запускаем задачу асинхронно
    task = send_order_notification_task.delay(latest_order.id)
    print(f"✅ Задача поставлена в очередь: {task.id}")
    print("Проверьте Celery worker для выполнения задачи")
    
    return True


if __name__ == '__main__':
    try:
        # Тестируем синхронную отправку
        test_telegram_notification()
        
        # Тестируем асинхронную задачу
        test_celery_task()
        
    except Exception as e:
        print(f"❌ Ошибка при тестировании: {e}")
        import traceback
