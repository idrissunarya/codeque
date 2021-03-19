from django.shortcuts import render, redirect, HttpResponse
from apps.api.models import Blog, Categori
from django.db.models import Q


def home(request):
    return render(request, 'web/index.html')

def signup(request):
    return render(request, 'web/pages/signup.html')

def login(request):
    return render(request, 'web/pages/login.html')

def explore_python_list(request):
    queryset = Categori.objects.filter(name='Python')
    context = {'queryset': queryset}
    return render(request,  'web/pages/navcat/explore_list.html', context)

def explore_python_detail(request, blog_id):
    queryset = Blog.objects.filter(blog_id=blog_id)
    context = {'queryset': queryset}
    return render(request, 'web/pages/navcat/explore_python_detail.html', context)

