from django.urls import path
from  . import views

app_name = 'posts'

urlpatterns = [
    path('posts_list/', views.posts_list, name='posts_list'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail')
]