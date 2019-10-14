from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('profile/', views.profile , name = 'profile_view'),
    path('post/del/<int:pk>' , views.post_del , name = 'post_del'),
]
