from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


from .models import Order
from cars.models import Car
from .tasks import send_order_notification_task
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@require_POST
@csrf_exempt  # Временно отключаем CSRF для AJAX, но лучше настроить правильно
def create_order(request, car_id):
    """Создание заказа через AJAX"""
    car = get_object_or_404(Car, id=car_id)
    
    try:
        # Пытаемся получить данные из JSON
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            full_name = data.get('full_name')
            phone = data.get('phone')
            agree = data.get('agree')
        else:
            # Или из обычной формы
            full_name = request.POST.get('full_name')
            phone = request.POST.get('phone')
        
        if not full_name or not phone:
            return JsonResponse({
                'success': False,
                'error': 'Пожалуйста, заполните все обязательные поля.'
            })
        
        
        # Создаем заказ
        order = Order.objects.create(
            car=car,
            full_name=full_name,
            phone=phone,
            total_amount=car.price,
            status='new'
        )
        
        # Отправляем уведомление в Telegram через Celery
        send_order_notification_task.delay(order.id)
        
        return JsonResponse({
            'success': True,
            'message': 'Спасибо за заказ! Мы свяжемся с вами в ближайшее время.',
            'order_id': order.id
        })
        
    except Exception as e:
        print(e)
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

def order_list(request):
    """Список заказов пользователя"""
    orders = Order.objects.filter().order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context)
