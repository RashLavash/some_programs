from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_main'),
    path('about', views.about_us, name='about_us')
]
