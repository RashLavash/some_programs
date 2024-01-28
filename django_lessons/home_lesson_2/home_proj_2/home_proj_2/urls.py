from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('my_app_1.urls', namespace='my_app_1')),
    path('admin/', admin.site.urls),
]
