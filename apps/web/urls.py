from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('explore/python/', views.explore_python_list, name='explore_python_list'),
    path('explore/python/<str:blog_id>/', views.explore_python_detail, name='explore_python_detail'),
]