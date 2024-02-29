from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('post_list/', views.APIPostList.as_view(), name='post_list'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
    # path('post_detail/<int:pk>/', views.APIPostDetail.as_view(), name='post_detail'),
    path('post_detail/<int:pk>/', views.PostList.as_view(), name='post_detail'),
]