from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('ourshops.html', views.ourshops, name='ourshops'),
    path('cats_toys.html', views.cats_toys, name='cats_toys'),
    path('cats_feed.html', views.cats_feed, name='cats_feed'),
    path('cats_acc.html', views.cats_acc, name='cats_acc'),
    path('dogs_toys.html', views.cats_toys, name='dogs_toys'),
    path('dogs_feed.html', views.cats_feed, name='dogs_feed'),
    path('dogs_acc.html', views.cats_acc, name='dogs_acc'),
    path('birds_toys.html', views.cats_toys, name='birds_toys'),
    path('birds_feed.html', views.cats_feed, name='birds_feed'),
    path('birds_acc.html', views.cats_acc, name='birds_acc')
]