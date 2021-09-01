from django.shortcuts import render
from django.contrib import redirects
from django.shortcuts import render
import random

# Create your views here.

def home(request):
    num = [str(i) for i in range(0, 10)]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    upper_char = list(alpha.upper())
    lower_char = list(alpha)
    spec_char = list('!@#&;?')

    l = upper_char + lower_char + spec_char + num
    random.shuffle(l)
    length = random.randint(8,15)
    r=''
    for i in range(0,length):
        r += random.choice(l)

    print(l)
    return render(request, 'generator/home.html', context={'list' : r})


def about(request):
    return render(request, 'generator/about.html')


def error(request ,invalid_url):
    return render(request, 'generator/Invalid.html', context={'url' : invalid_url})