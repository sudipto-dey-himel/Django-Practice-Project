from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:blog_id>/edit/', views.edit, name='edit'),
    path('<int:blog_id>/delete/', views.delete, name='delete'),
    path('register/', views.register, name="register")
]