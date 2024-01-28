from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main'),
    path('posts_list/', views.posts_list, name='posts_list'),
    path('posts_detail/<int:id>/', views.posts_detail, name='posts_detail'),
]
