from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, './frames_site/index.html')


def about(request):
    return render(request, './frames_site/about.html')
