from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:pk>/', views.car_detail, name='car_detail'),
    path('contacts/', views.contacts, name='contacts'),
]
