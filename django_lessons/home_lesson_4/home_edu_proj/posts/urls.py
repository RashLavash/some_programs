from django.urls import path
from .views import PostList, PostDetail


urlpatterns = [
    path('post_list/', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
]