from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('', views.index),
    path('posts_list/', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
