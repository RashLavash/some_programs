from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    # context = []
    # context['username'] = 'RashidbeG'

    return render(request, 'posts/index.html')

def greet_user(request, name):
    return HttpResponse(f'hello user! {name}')

def greet(request):
    return HttpResponse('hello rash')


