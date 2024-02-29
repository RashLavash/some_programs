from django.urls import path
# from .views import PostDetail, PostList
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    # path('', PostListAPIView.as_view(), name='post_list'),
]