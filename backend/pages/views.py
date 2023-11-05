from django.shortcuts import render

# Create your views here.
def home_page(request):
    pass

def about_page(request):
    return render(request, 'pages/about.html')

def tos_page(request):
    return render(request, 'pages/tos.html')

def privacy_page(request):
    return render(request, 'pages/privacy.html')

