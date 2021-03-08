from django.shortcuts import render, redirect

def home(request):
    return render(request, 'web/index.html')

def signup(request):
    return render(request, 'web/pages/signup.html')

def login(request):
    return render(request, 'web/pages/login.html')
