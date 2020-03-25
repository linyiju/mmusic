from blog.views import post_detail, post_edit, post_list, post_new
from django.urls import path

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
]
