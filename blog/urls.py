from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    parth('post/remove/<int:pk>/', views.post_del , name='post_del'),
]
