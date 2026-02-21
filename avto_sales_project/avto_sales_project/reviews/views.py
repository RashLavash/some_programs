from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Review
from cars.models import Car


def reviews_list(request):
    """Список отзывов"""
    reviews = Review.objects.filter(is_approved=True).order_by('-created_at')
    
    paginator = Paginator(reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'reviews/reviews.html', context)


@login_required
def add_review(request, car_id):
    """Добавление отзыва"""
    car = get_object_or_404(Car, id=car_id)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        
        if not rating or not text:
            messages.error(request, 'Пожалуйста, заполните все поля.')
            return redirect('reviews')
        
        # Проверяем, не оставлял ли пользователь уже отзыв на этот автомобиль
        existing_review = Review.objects.filter(car=car, user=request.user).first()
        if existing_review:
            messages.error(request, 'Вы уже оставляли отзыв на этот автомобиль.')
            return redirect('reviews')
        
        review = Review.objects.create(
            car=car,
            user=request.user,
            rating=rating,
            text=text,
            is_approved=False  #
        )
        
        messages.success(request, 'Спасибо за ваш отзыв! Он будет опубликован после модерации.')
        return redirect('reviews')
    
    return redirect('reviews')
