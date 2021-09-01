from django.shortcuts import render
from django.contrib import redirects
from django.shortcuts import render


# Create your views here.

def home(request):
    num = [i for i in range(0, 10)]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    upper_char = list(alpha.upper())
    lower_char = list(alpha)
    spec_char = list('!@#^&*;?<>')
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')

def error(request ,invalid_url):
    return render(request, 'generator/home.html')