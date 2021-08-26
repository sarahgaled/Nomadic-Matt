from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs_index, name="blog_index"),
    path('blogs/<int:blog_id>/', views.blogs_detail, name="blogs_detail"),
    path('blogs/create/', views.BlogCreate.as_view(), name='blogs_create'),
]
