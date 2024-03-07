from rest_framework.routers import DefaultRouter

from django.urls import path, include

from . import views


router = DefaultRouter()


router.register(r'posts', views.PostViewSet, basename='my_posts')


urlpatterns = [
    path('', include(router.urls))
]