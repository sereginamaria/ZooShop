from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as log_in, logout as log_out
from django.db.models import Q
from web.models import Client, Item
from mysite.settings import BASE_DIR
import random
import os


def index(request):
    # limit 10
    items = Item.objects.filter(img_path__contains='toy')
    random_items = random.sample(list(items), 6)

    items1 = Item.objects.filter(img_path__contains='feed')
    random_items1 = random.sample(list(items1), 6)

    items2 = Item.objects.filter(img_path__contains='acc')
    random_items2 = random.sample(list(items2), 6)

    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username,
               'items': random_items,
               'items1': random_items1,
               'items2': random_items2,}
    return render(request, 'web/index.html', context=context)


def about(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/about.html', context=context)


def ourshops(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/ourshops.html', context=context)


def cats_toys(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/cats_toys.html', context=context)


def cats_feed(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/cats_feed.html', context=context)


def cats_acc(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/cats_acc.html', context=context)


def dogs_toys(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/dogs_toys.html', context=context)


def dogs_feed(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/dogs_feed.html', context=context)


def dogs_acc(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/dogs_acc.html', context=context)


def birds_toys(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/birds_toys.html', context=context)


def birds_feed(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/birds_feed.html', context=context)


def birds_acc(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/birds_acc.html', context=context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log_in(request, user)
            return redirect('web:index')
        return render(request, 'web/login.html')
    else:
        return render(request, 'web/login.html')


def logout(request):
    log_out(request)
    return redirect(request.META.get('HTTP_REFERER'))


def registration(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/registration.html', context=context)


def cart(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/cart.html', context=context)


def signup(request):
    if request.method == 'POST':
        post = request.POST
        username = post['name']
        password = post['password']
        email = post['email']
        last_name = post['surname']
        phone = post['phone']
        user = Client.objects.create_user(username, email, password,
                                          last_name=last_name, phone=phone)
        log_in(request, user)
        return redirect('web:index')
    else:
        return redirect('web:registration')


def products(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    context = {'username': username}
    return render(request, 'web/products.html', context=context)