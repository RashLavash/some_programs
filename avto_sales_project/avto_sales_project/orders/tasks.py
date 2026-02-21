from celery import shared_task
import requests
import json
from django.conf import settings


@shared_task
def send_order_notification_task(order_id):
    """
    Асинхронная задача Celery для отправки уведомления в Telegram
    """
    from .models import Order
    
    try:
        # Получаем заказ из базы данных
        order = Order.objects.get(id=order_id)
        
        # Настройки Telegram бота (замените на свои)
        BOT_TOKEN = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
        CHAT_ID = getattr(settings, 'TELEGRAM_CHAT_ID', None)
        
        if not BOT_TOKEN or not CHAT_ID:
            # Если токен не настроен, просто логируем
            print(f"Telegram не настроен. Новый заказ: {order}")
            return False
       
        message = f"""
Новый заказ на автомобиль! 🚗

Автомобиль: {order.car.brand.name} {order.car.model}
Клиент: {order.full_name}
Телефон: {order.phone}
Сумма: {order.total_amount} ₽
Дата: {order.created_at.strftime('%d.%m.%Y %H:%M')}

Статус: {order.get_status_display()}

"""
        
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        data = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML',
        }
        
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 200:
            print(f"Сообщение в Telegram отправлено успешно для заказа {order_id}")
            return True
        else:
            print(f"Ошибка отправки в Telegram для заказа {order_id}: {response.status_code}")
            return False
            
    except Order.DoesNotExist:
        print(f"Заказ с ID {order_id} не найден")
        return False
    except Exception as e:
        print(e.args)
        print(f"Ошибка при отправке уведомления для заказа {order_id}: {e}")
        return False
