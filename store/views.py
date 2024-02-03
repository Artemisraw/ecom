from django.shortcuts import render
from .models import Product
from .forms import CreateUserForm



# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def login(request):

    login_url = '../templates/accounts/login.html/'
    return render(request, login_url)

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    register_url = '../templates/accounts/register.html/'
    return render(request, register_url, context)

def about(request):
    return render(request, 'about.html',{})
