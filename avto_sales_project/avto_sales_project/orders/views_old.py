from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order
from cars.models import Car


@login_required
def create_order(request, car_id):
    """Создание заказа"""
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        
        if not full_name or not phone:
            messages.error(request, 'Пожалуйста, заполните все обязательные поля.')
            return redirect('cars:car_detail', pk=car_id)
        
        # Создаем заказ
        order = Order.objects.create(
            car=car,
            full_name=full_name,
            phone=phone,
            total_amount=car.price,
            status='new'
        )
        
        # Отправляем уведомление в Telegram
        send_order_notification(order)
        
        messages.success(request, 'Спасибо за заказ! Мы свяжемся с вами в ближайшее время.')
        return redirect('cars:car_detail', pk=car_id)
    
    return redirect('cars:car_detail', pk=car_id)


def send_order_notification(order):
    """Отправка уведомления в Telegram"""
    import requests
    
    # Настройки Telegram бота (замените на свои)
    BOT_TOKEN = 'YOUR_BOT_TOKEN'
    CHAT_ID = 'YOUR_CHAT_ID'
    
    if BOT_TOKEN == 'YOUR_BOT_TOKEN' or CHAT_ID == 'YOUR_CHAT_ID':
        # Если токен не настроен, просто логируем
        print(f"Новый заказ: {order}")
        return
    
    message = f"""
Новый заказ на автомобиль!

🚗 Автомобиль: {order.car.brand.name} {order.car.model}
👤 Клиент: {order.full_name}
📞 Телефон: {order.phone}
💰 Сумма: {order.total_amount} ₽
📅 Дата: {order.created_at.strftime('%d.%m.%Y %H:%M')}

Статус: {order.get_status_display()}
"""
    
    try:
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        data = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Сообщение в Telegram отправлено успешно")
        else:
            print(f"Ошибка отправки в Telegram: {response.status_code}")
    except Exception as e:
        print(f"Ошибка при отправке в Telegram: {e}")


@login_required
def order_list(request):
    """Список заказов пользователя"""
    orders = Order.objects.filter(full_name=request.user.get_full_name() or request.user.username).order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context)
