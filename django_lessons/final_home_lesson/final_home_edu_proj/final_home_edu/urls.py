from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/news/', include(('news.urls', 'news'), namespace='news')),
    # path('api/v1/posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('admin/', admin.site.urls),
]
