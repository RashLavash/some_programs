from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('auth/', include(('users.urls', 'users'), namespace='users')),
    path('posts/', include(('posts.urls', 'posts'), namespace='posts')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

handler404 = 'core.views.page_not_found'