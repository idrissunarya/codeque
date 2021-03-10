from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import BlogListView
from apps.api import views

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<uuid:pk>/', views.blog_detail),
]