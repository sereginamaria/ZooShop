from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    return HttpResponse('Hello, world!')


def index(request):
    return render(request, 'web/index.html')


def about(request):
    return render(request, 'web/about.html')


def ourshops(request):
    return render(request, 'web/ourshops.html')


def cats_toys(request):
    return render(request, 'web/cats_toys.html')


def cats_feed(request):
    return render(request, 'web/cats_feed.html')


def cats_acc(request):
    return render(request, 'web/cats_acc.html')


def dogs_toys(request):
    return render(request, 'web/dogs_toys.html')


def dogs_feed(request):
    return render(request, 'web/dogs_feed.html')


def dogs_acc(request):
    return render(request, 'web/dogs_acc.html')


def birds_toys(request):
    return render(request, 'web/birds_toys.html')


def birds_feed(request):
    return render(request, 'web/birds_feed.html')


def birds_acc(request):
    return render(request, 'web/birds_acc.html')


def login(request):
    return render(request, 'web/login.html')


def registration(request):
    return render(request, 'web/registration.html')


def card():
    return render(request, 'web/card.html')