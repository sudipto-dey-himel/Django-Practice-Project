from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('explore/', views.blog_list, name='blog_list'),
    path('create/', views.create, name='create'),
    path('<int:blog_id>/edit/', views.edit, name='edit'),
    path('<int:blog_id>/delete/', views.delete, name='delete'),
    path('register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
] 