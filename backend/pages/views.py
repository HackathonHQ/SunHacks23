from django.shortcuts import render

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