from django.urls import path
from . import views


app_name = 'my_app_1'

urlpatterns = [
    path('', views.index, name='index'),
    path('workers', views.workers, name='workers'),
    path('add_worker', views.add_worker, name='add_worker'),
]