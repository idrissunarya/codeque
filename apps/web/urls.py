from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('explore/python/search/', views.search_python, name='search_python'),
    path('explore/python/', views.explore_python_list, name='explore_python_list'),
    path('explore/python/<slug:slug>/', views.explore_python_detail, name='explore_pyton_detail'),
    path('explore/nginx/', views.explore_nginx_list, name='explore_nginx_list'),
    path('explore/nginx/<slug:slug>/', views.explore_nginx_detail, name='explore_nginx_detail'),
]


    
