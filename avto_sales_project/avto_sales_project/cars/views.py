from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Car, Brand, PriceCategory


def home(request):
    """Главная страница"""
    cars = Car.objects.filter(is_active=True)[:6]
    context = {
        'cars': cars,
    }
    return render(request, 'cars/home.html', context)


def catalog(request):
    """Каталог автомобилей с фильтрацией"""
    cars = Car.objects.filter(is_active=True)
    
    # Фильтрация по цене
    price_filter = request.GET.get('price')
    if price_filter:
        if price_filter == '1000000':
            cars = cars.filter(price__lte=1000000)
        elif price_filter == '5000000':
            cars = cars.filter(price__lte=5000000)
        elif price_filter == '10000000':
            cars = cars.filter(price__lte=10000000)
        elif price_filter == '50000000':
            cars = cars.filter(price__lte=50000000)
    
    # Фильтрация по маркам
    brand_filter = request.GET.getlist('brands')
    if brand_filter:
        cars = cars.filter(brand__id__in=brand_filter)
    
    # Поиск
    search_query = request.GET.get('search')
    if search_query:
        cars = cars.filter(
            Q(brand__name__icontains=search_query) |
            Q(model__icontains=search_query) |
            Q(year__icontains=search_query)
        )
    
    # Сортировка
    sort_by = request.GET.get('sort', '-created_at')
    cars = cars.order_by(sort_by)
    
    # Пагинация
    paginator = Paginator(cars, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Получаем все марки для фильтра
    brands = Brand.objects.all()
    
    context = {
        'page_obj': page_obj,
        'brands': brands,
        'price_filter': price_filter,
        'brand_filter': [int(b) for b in brand_filter],
        'search_query': search_query,
        'sort_by': sort_by,
    }
    
    return render(request, 'cars/catalog.html', context)


def car_detail(request, pk):
    """Детали автомобиля"""
    car = get_object_or_404(Car, pk=pk, is_active=True)
    context = {
        'car': car,
    }
    return render(request, 'cars/car_detail.html', context)


def contacts(request):
    """Страница контактов"""
    return render(request, 'cars/contacts.html')
