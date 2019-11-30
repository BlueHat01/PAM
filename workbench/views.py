from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'RP1' ,
        'title' : 'BG-1' ,
        'content' : 'CONTENT 1' ,
        'date_posted' : '12th NOV 2019'
    },
    {
        'author': 'RP2',
        'title': 'BG-2',
        'content': 'CONTENT 2',
        'date_posted': '13th NOV 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'workbench/home.html', context)


def about(request):
    return render(request, 'workbench/about.html')


# Create your views here.
