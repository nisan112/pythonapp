from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth import views as auth_views
from index import views

urlpatterns = [
    path("", views.start, name="start"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),  # This will be the homepage URL
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('search/', views.search_posts, name='search_posts'),  # New URL for search
path('logout/', auth_views.LogoutView.as_view(), name='logout'),




]