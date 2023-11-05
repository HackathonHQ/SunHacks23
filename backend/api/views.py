from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from inventory.models import Item
# Create your views here.
def status(request):
    return  JsonResponse({'status': 'ok'})

def get_items(request, search=None):
    if search:
        items = Item.objects.filter(name__icontains=search)
    else:
        items = Item.objects.all()
    return JsonResponse({'items': [item.to_json() for item in items]})


def get_item(request, id):
    item = Item.objects.get(id=id)
    return JsonResponse({'item': item.to_json()})

def create_item(request):
    item = Item.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
        price=request.POST['price'],
        image=request.POST['image'],
        owner=request.user
    )
    return JsonResponse({'item': item.to_json()})

def update_item(request, id):
    item = Item.objects.get(id=id)
    if request.POST.get('name'):
        item.name = request.POST['name']
    if request.POST.get('description'):
        item.description = request.POST['description']
    if request.POST.get('price'):
        item.price = request.POST['price']
    if request.POST.get('image'):
        item.image = request.POST['image']
    item.save()
    return JsonResponse({'item': item.to_json()})

def login(request):
    pass
