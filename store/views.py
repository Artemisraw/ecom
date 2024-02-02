from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def login(request):
    login_url = '../templates/registration/login.html/'
    return render(request, login_url)

def register(request):
    register_url = '../templates/registration/register.html/'
    return render(request, register_url)