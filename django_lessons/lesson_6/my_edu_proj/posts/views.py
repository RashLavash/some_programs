from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post


def index(request):
    return render(request, 'posts/index.html')


def posts_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)
    page_1 = paginator.page(1)
    print(page_1.object_list)
    page_num = request.GET.get('page')
    print(page_num)


    page_obj = paginator.get_page(page_num)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):
    posts = Post.objects.get(id=id)
    context = {
        'current_id': id,
        'posts': posts
    }
    return render(request, 'posts/posts_detail.html', context)

