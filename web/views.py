from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    return HttpResponse('Hello, world!')


def index(request):
    return render(request, '../templates/web/index.html')


def about(request):
    return render(request, '../templates/web/about.html')


def ourshops(request):
    return render(request, '../templates/web/ourshops.html')


def cats_toys(request):
    return render(request, '../templates/web/cats_toys.html')


def cats_feed(request):
    return render(request, '../templates/web/cats_feed.html')


def cats_acc(request):
    return render(request, '../templates/web/cats_acc.html')


def dogs_toys(request):
    return render(request, '../templates/web/dogs_toys.html')


def dogs_feed(request):
    return render(request, '../templates/web/dogs_feed.html')


def dogs_acc(request):
    return render(request, '../templates/web/dogs_acc.html')


def birds_toys(request):
    return render(request, '../templates/web/birds_toys.html')


def birds_feed(request):
    return render(request, '../templates/web/birds_feed.html')


def birds_acc(request):
    return render(request, '../templates/web/birds_acc.html')

