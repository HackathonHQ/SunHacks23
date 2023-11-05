from django.contrib import admin 
from django.urls import path, include
from .views import status, login
urlpatterns = [
    path('status/', view=status), 
    path('login/', view=login)
]
