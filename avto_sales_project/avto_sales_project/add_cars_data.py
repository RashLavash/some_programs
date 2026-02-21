#!/usr/bin/env python
"""
Скрипт для добавления марок и автомобилей в базу данных
"""

import os
import sys
import django

# Настройка Django окружения
sys.path.append('/home/nariman079i/NotiesBooks/github/RasidBack/avto_sales_project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avto_sales.settings')
django.setup()

from cars.models import Brand, PriceCategory, Car, CarImage

def add_brands():
    """Добавление марок автомобилей"""
    brands_data = [
        'Hyundai', 'Lada', 'Volkswagen', 'Honda', 'BMW', 'Mersedes', 'Rolls-Roys',
        'Bently', 'Geely', 'Akura', 'Changan', 'Omoda', 'Jtour', 'Haval', 'Exeed',
        'Chevrolet', 'Ford', 'Ferrary', 'Lamborghini', 'Audi', 'Porshe', 'Dodge',
        'Koenigsegg', 'Volvo', 'Kia', 'Mazda', 'Toyota'
    ]
    
    created_brands = []
    for brand_name in brands_data:
        brand, created = Brand.objects.get_or_create(
            name=brand_name,
            defaults={
                'description': f'Автомобили марки {brand_name}'
            }
        )
        if created:
            created_brands.append(brand_name)
            print(f"✅ Добавлена марка: {brand_name}")
        else:
            print(f"ℹ️  Марка уже существует: {brand_name}")
    
    return Brand.objects.all()

def add_price_categories():
    """Добавление ценовых категорий"""
    categories_data = [
        {'name': 'Эконом', 'max_price': 1000000, 'description': 'Автомобили до 1 миллиона'},
        {'name': 'Средний', 'max_price': 3000000, 'description': 'Автомобили до 3 миллионов'},
        {'name': 'Премиум', 'max_price': 10000000, 'description': 'Автомобили до 10 миллионов'},
        {'name': 'Люкс', 'max_price': 50000000, 'description': 'Автомобили до 50 миллионов'},
    ]
    
    for cat_data in categories_data:
        category, created = PriceCategory.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'max_price': cat_data['max_price'],
                'description': cat_data['description']
            }
        )
        if created:
            print(f"✅ Добавлена категория: {cat_data['name']} (до {cat_data['max_price']} ₽)")
        else:
            print(f"ℹ️  Категория уже существует: {cat_data['name']}")

def add_cars():
    """Добавление автомобилей"""
    # Получаем все марки и категории
    brands = Brand.objects.all()
    categories = PriceCategory.objects.all()
    
    # Примеры моделей для каждой марки
    models_by_brand = {
        'Hyundai': ['Elantra', 'Solaris', 'Creta', 'Tucson', 'Santa Fe'],
        'Lada': ['Granta', 'Vesta', 'Niva', 'Kalina', 'Priora'],
        'Volkswagen': ['Polo', 'Jetta', 'Tiguan', 'Passat', 'Golf'],
        'Honda': ['Civic', 'Accord', 'CR-V', 'HR-V', 'Fit'],
        'BMW': ['3 Series', '5 Series', 'X3', 'X5', 'X1'],
        'Mersedes': ['C-Class', 'E-Class', 'GLC', 'GLE', 'A-Class'],
        'Rolls-Roys': ['Phantom', 'Ghost', 'Cullinan', 'Wraith', 'Dawn'],
        'Bently': ['Continental', 'Flying Spur', 'Bentayga', 'Mulsanne'],
        'Geely': ['Atlas', 'Monjaro', 'Emgrand', 'Coolray', 'Tugella'],
        'Akura': ['TLX', 'RDX', 'MDX', 'ILX', 'NSX'],
        'Changan': ['CS75', 'CS55', 'CS35', 'Eado', 'Raeton'],
        'Omoda': ['O5', 'C5', 'C7', 'E5', 'S5'],
        'Jtour': ['T8', 'T9', 'T6', 'X7', 'X9'],
        'Haval': ['H6', 'F7', 'Big Dog', 'M6', 'Dargo'],
        'Exeed': ['LX', 'TXL', 'RX', 'VX', 'TX'],
        'Chevrolet': ['Cruze', 'Cobalt', 'Captiva', 'Lacetti', 'Nexia'],
        'Ford': ['Focus', 'Fiesta', 'Escape', 'Fusion', 'EcoSport'],
        'Ferrary': ['488', 'Portofino', 'Roma', 'SF90', '812'],
        'Lamborghini': ['Huracan', 'Urus', 'Aventador', 'Huracan STO'],
        'Audi': ['A4', 'A6', 'Q5', 'Q7', 'A3'],
        'Porshe': ['911', 'Cayenne', 'Macan', 'Panamera', 'Taycan'],
        'Dodge': ['Challenger', 'Charger', 'Durango', 'Journey', 'Ram'],
        'Koenigsegg': ['Jesko', 'Gemera', 'Regera', 'Agera'],
        'Volvo': ['XC90', 'XC60', 'S90', 'V90', 'S60'],
        'Kia': ['Rio', 'Sportage', 'Sorento', 'Cerato', 'Optima'],
        'Mazda': ['3', '6', 'CX-5', 'CX-30', 'MX-5'],
        'Toyota': ['Camry', 'Corolla', 'RAV4', 'Land Cruiser', 'Hilux']
    }
    
    # Типы двигателей
    engine_types = ['gasoline', 'diesel', 'hybrid', 'electric']
    
    # Коробки передач
    transmissions = ['manual', 'automatic', 'robot', 'variator']
    
    # Приводы
    drives = ['front', 'rear', 'all']
    
    # Цвета
    colors = ['Белый', 'Черный', 'Серебристый', 'Синий', 'Красный', 'Серый', 'Зеленый']
    
    created_count = 0
    for brand in brands:
        brand_models = models_by_brand.get(brand.name, [f'Model {i+1}' for i in range(3)])
        
        for i, model in enumerate(brand_models[:3]):  # Берем по 3 модели на марку
            # Определяем ценовую категорию по марке
            if brand.name in ['Ferrary', 'Lamborghini', 'Rolls-Roys', 'Bently', 'Koenigsegg', 'Porshe']:
                category = categories.filter(name='Люкс').first()
                price = 20000000 + (i * 5000000)
            elif brand.name in ['BMW', 'Mersedes', 'Audi', 'Volvo', 'Mazda']:
                category = categories.filter(name='Премиум').first()
                price = 5000000 + (i * 1500000)
            elif brand.name in ['Hyundai', 'Honda', 'Kia', 'Toyota', 'Ford', 'Chevrolet']:
                category = categories.filter(name='Средний').first()
                price = 1500000 + (i * 500000)
            else:
                category = categories.filter(name='Эконом').first()
                price = 800000 + (i * 200000)
            
            year = 2020 + (i % 5)  # Год от 2020 до 2024
            engine_type = engine_types[i % len(engine_types)]
            transmission = transmissions[i % len(transmissions)]
            drive = drives[i % len(drives)]
            color = colors[(i + hash(brand.name)) % len(colors)]
            mileage = 10000 + (i * 15000)
            power = 120 + (i * 50)
            engine_volume = 1.6 + (i * 0.5)
            
            description = f'Автомобиль {brand.name} {model} {year} года выпуска. Отличное состояние, все ТО пройдены.'
            
            car, created = Car.objects.get_or_create(
                brand=brand,
                model=model,
                year=year,
                defaults={
                    'price': price,
                    'engine_volume': round(engine_volume, 1),
                    'engine_type': engine_type,
                    'transmission': transmission,
                    'drive': drive,
                    'color': color,
                    'mileage': mileage,
                    'power': power,
                    'description': description,
                    'category': category,
                    'is_active': True
                }
            )
            
            if created:
                created_count += 1
                print(f"✅ Добавлен автомобиль: {brand.name} {model} ({year}) - {price:,} ₽")
            else:
                print(f"ℹ️  Автомобиль уже существует: {brand.name} {model} ({year})")
    
    print(f"\n🎉 Всего добавлено автомобилей: {created_count}")

def main():
    """Основная функция"""
    print("🚀 Начинаем добавление данных в базу...\n")
    
    print("1. Добавление марок:")
    add_brands()
    
    print("\n2. Добавление ценовых категорий:")
    add_price_categories()
    
    print("\n3. Добавление автомобилей:")
    add_cars()
    
    print("\n✅ Все данные успешно добавлены в базу данных!")

if __name__ == '__main__':
    main()