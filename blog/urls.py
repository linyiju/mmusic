from blog import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
]
