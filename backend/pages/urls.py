from django.contrib import admin 
from django.urls import path, include
from . import views
urlpatterns = [
    path('',  views.home_page, name='home'),
    path('logged_in/',  views.logged_in, name='logged_in'),
    path('list/',  views.list, name='list'),
]
