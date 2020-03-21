from django.urls import path

from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detial, name='post_detial')
]
