from django.contrib import admin 
from django.urls import path, include
from .views import home_page, about_page, tos_page, privacy_page
urlpatterns = [
    path('', home_page),


]
