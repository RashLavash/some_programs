from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, document_root=
#     )

# <a href="{% 'posts:posts_list' %}">Текст</a>