from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import BlogListView
from apps.api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<uuid:pk>/', views.blog_detail),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)