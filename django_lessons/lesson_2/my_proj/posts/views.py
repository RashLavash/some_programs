from django.shortcuts import render

from django.http import HttpResponse

from .forms import PostForm


def index(request):
    context = {'user_name': 'Rash'}
    return render(request, 'index.html', context)


def posts_list(request):

    return render(request, 'posts_list.html')


def posts_detail(request, pk):
    context = {'user_name': pk}
    return render(request, 'posts_detail.html', context)


def posts_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            date = form.cleaned_data['date']
            
            return HttpResponse(f'{title} {text} {date}')
    else:
        form = PostForm()
    context = {'form': form}

    return render(request, 'form.html', context)
