from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include(('posts.urls', 'posts'), namespace='posts')),
    path('admin/', admin.site.urls),
]
