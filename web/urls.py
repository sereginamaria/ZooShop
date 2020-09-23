from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('ourshops', views.ourshops, name='ourshops'),
    path('cats_toys', views.cats_toys, name='cats_toys'),
    path('cats_feed', views.cats_feed, name='cats_feed'),
    path('cats_acc', views.cats_acc, name='cats_acc'),
    path('dogs_toys', views.dogs_toys, name='dogs_toys'),
    path('dogs_feed', views.dogs_feed, name='dogs_feed'),
    path('dogs_acc', views.dogs_acc, name='dogs_acc'),
    path('birds_toys', views.birds_toys, name='birds_toys'),
    path('birds_feed', views.birds_feed, name='birds_feed'),
    path('birds_acc', views.birds_acc, name='birds_acc'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name="registration"),
    path('card', views.card, name='card')
]