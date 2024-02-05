from django.shortcuts import render
from django.db.models import Max, Min, Sum, Count, Avg

from .forms import PostForm
from .models import Post, User


def index(request):
    return render(request, 'posts/index.html')


def posts_list(request):
    # Считывание записи
    user = User.objects.get(id=1)
    # Создание записи
    # post = Post.objects.create(title='Rash', text='lavash', author=user)    
    # post = Post.objects.get_or_create(title='Rash', text='lavash', author=user)    
    post = Post.objects.get(id=1)    
    # Изменение записи
    post.text = 'измененный текст'
    # print(post.text)
    # posts = Post.objects.all()
    # Удаление публикации
    # post.delete()

    # posts = Post.objects.exclude(title='Заголовок2') исключаем публикацию по названию
    posts = Post.objects.filter(author=user)
    # contains - поле должно содержать
    posts = Post.objects.filter(title__contains='R')
    # Поле начинается на startswith, заканчивается на endswith
    # posts = Post.objects.filter(text__startswith='lava')
    # posts = Post.objects.filter(text__endswith='lava')
    # in - проверка вхождения
    post = Post.objects.filter(title__in=('Rash', 'Заг'))
    # range - проверяем на вхождение в интервал
    post = Post.objects.filter(title__range=(1, 4))
    # gt, gte, lt, lte - операции сравнения >, <, >=, <= 
    post = Post.objects.filter(id__gte=1)
    # year, month, day, week, hour, week_day, time, minute, second - 
    # post = Post.objects.filter(pub_date__hour=час)
    post = Post.objects.filter(
        text__startswith='R'
        ).filter(
            text__endswith='h'
        )
    # Фильтруем поля которые связаны внешним ключем
    post = Post.objects.filter(author__username='Rash')

    # Сортировка объектов
    post = Post.objects.filter(author__username='Rash').order_by('pub_date')[1:] # последние 1 записей
    # post = Post.objects.filter(author__username='Rash').order_by('-pub_date')[:10] # последние 10 записей
    
    # Исключение отдельных полей - defer
    post = Post.objects.defer('author')
    
    post = Post.objects.count() # подсчитываем количество записей

    # Агрегирующие фуункции
    print(Post.objects.aggregate(Max('id')))
    print(Post.objects.aggregate(Avg('id')))

    User.objects.annotate(posts_avg=Avg('posts__id')) # posts_avg - придуманное поле


    context = {
        'current_id': 5,
        'form': PostForm,
        'posts': posts
    }
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):

    post = Post.objects.get(id=id)
    context = {
        'post': post,
        'id': id
    }

    return render(request, 'posts/posts_detail.html', context)
