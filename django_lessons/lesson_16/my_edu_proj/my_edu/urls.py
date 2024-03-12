from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('auth/', include('rest_framework.urls')),

    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
    
    path('admin/', admin.site.urls),
]
