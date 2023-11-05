from django.shortcuts import render
from inventory.models import Item
# Create your views here.
def home_page(request):
    print("HTML Index")
    context ={
        "provider_login_url":"api/v1/login/"
    }
    return render(request, "../templates/index.html", context=context)
def about_page(request):
    return render(request, 'pages/about.html')

def tos_page(request):
    return render(request, 'pages/tos.html')

def privacy_page(request):
    return render(request, 'pages/privacy.html')

def logged_in(request):
    return render(request, '../templates/logged_in.html')

def list(request):
    return render(request, '../templates/list.html')

def search(request, keyword):
     items = Item.objects.filter(name__icontains=keyword)
     context = {
            'items': items,
            'keyword': keyword
        }
     
