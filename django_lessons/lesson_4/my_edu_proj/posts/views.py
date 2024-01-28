from django.shortcuts import render
from .forms import PostForm


def index(request):
    return render(request, 'posts/index.html')


def posts_list(request):
    context = {
        'current_id': 5,
        'form': PostForm
    }
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):

    context = {
        'id': id
    }

    return render(request, 'posts/posts_detail.html', context)
