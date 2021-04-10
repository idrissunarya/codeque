from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from apps.api.models import Blog, Categori, Course, Wiki
from django.db.models import Q

import emoji
import sys
from termcolor import colored, cprint

from django.db import connection
from prettytable import PrettyTable


def home(request):
    return render(request, 'web/index.html')

def signup(request):
    return render(request, 'web/pages/signup.html')

def login(request):
    return render(request, 'web/pages/login.html')


def explore_python_list(request):
    wiki_info = Wiki.objects.all()
    python_framework_count = Categori.objects.filter(name='bbc2a060-e615-484b-8eb9-de8c548cf386').count()
    python_module_count = Categori.objects.filter(name='21d7230a-a506-40d7-aa2a-b2d9620a0dfa').count()
    total_post = python_framework_count + python_module_count
    queryset = Categori.objects.filter(name='bbc2a060-e615-484b-8eb9-de8c548cf386').order_by('-created')
    query_module = Categori.objects.filter(name='21d7230a-a506-40d7-aa2a-b2d9620a0dfa')
    text = 'python'

    context = {
        'text': text,
        'wiki_info': wiki_info,
        'query_module': query_module,
        'total_post': total_post,
        'queryset': queryset,
        }

    return render(request,  'web/pages/navcat/explore_list.html', context)


def search_python(request):
    text = 'mode pencarian...'
    query_search = request.GET.get('q')
    if query_search:
        o1 = Categori.objects.filter(name='bbc2a060-e615-484b-8eb9-de8c548cf386')
        o2 = Categori.objects.filter(name='21d7230a-a506-40d7-aa2a-b2d9620a0dfa')
        queue_1 = o1.filter(Q(slug__icontains=query_search)).order_by('-created')
        queue_2 = o2.filter(Q(slug__icontains=query_search)).order_by('-created')
        print(queue_1)
        print(queue_2)
    else:
        o1 = Categori.objects.filter(name='bbc2a060-e615-484b-8eb9-de8c548cf386')
        o2 = Categori.objects.filter(name='21d7230a-a506-40d7-aa2a-b2d9620a0dfa')
        queue_1 = o1.all()
        queue_2 = o2.all()

    if query_search is None:
        return HttpResponse('No search query data given')

    context = {
        
    }

    return render(request, 'web/pages/search.html', {'queue_1': queue_1, 'queue_2': queue_2, 'query_search': query_search})
    

def explore_python_detail(request, slug):
    queryset = Blog.objects.filter(slug=slug)
    print(queryset)
    context = {'queryset': queryset}
    return render(request, 'web/pages/navcat/explore_detail.html', context)

def explore_nginx_list(request):
    wiki_info = Wiki.objects.filter(id=2)
    nginx_configure_count = Categori.objects.filter(name='6b01dde3-387e-4be3-be33-b14d203bc2f0').count()
    nginx_module_count = Categori.objects.filter(name='4a4ee8f7-86fa-446c-b14c-e1d0be32a014').count()
    total_post = nginx_configure_count + nginx_module_count
    queryset = Categori.objects.filter(name='6b01dde3-387e-4be3-be33-b14d203bc2f0').order_by('-created')
    query_module = Categori.objects.filter(name='4a4ee8f7-86fa-446c-b14c-e1d0be32a014').order_by('-created')
    text = 'nginx'

    print(total_post)


    output_print_1 = colored('Total Posts Nginx :', 'yellow', attrs=['reverse', 'blink'])
    output_print_2 = colored('Tag Query 1 :', 'yellow', attrs=['reverse', 'blink'])
    output_print_3 = colored('Tag Query 2 :', 'yellow', attrs=['reverse', 'blink'])
    output_print_4 = colored('Data Query :', 'yellow', attrs=['reverse', 'blink'])
    print(" ")
    print(output_print_1, "\N{barber pole} ", colored(total_post, 'green')+ ' Posts')
    print(" ")
    print(output_print_4, "\N{books} ", colored (queryset, 'green'))
    print(" ")
    #print(queryset)
    context = {'queryset': queryset, 'text': text, 'total_post': total_post, 'wiki_info': wiki_info, 'query_module': query_module}
    return render(request, 'web/pages/navcat/explore_list.html', context)


def explore_nginx_detail(request, slug):
    queryset = Blog.objects.filter(slug=slug)
    context = {'queryset': queryset,}
    return render(request, 'web/pages/navcat/explore_detail.html', context)

