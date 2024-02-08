from django.shortcuts import render, redirect
from .models import Product, User
from .forms import CreateUserForm, CreateLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages



# Create your views here.
# @login_required(login_url = 'login')
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            Firstname = form.cleaned_data.get('fName')
            Lastname = form.cleaned_data.get('lName')
            messages.success(request, 'Account created ' + Firstname +" " +Lastname)
            return redirect('login')
        
    context = {'form':form}
    register_url = '../templates/accounts/register.html/'
    return render(request, register_url, context)

# TODO: login url
def loginPage(request):
    form = CreateLoginForm()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, email)
            redirect('home')
        else:
            messages.info(request, 'Email or Password is incorrect. \n Please Try again')
            redirect('login')
    
    context = {'form':form}
    login_url = '../templates/accounts/login.html/'
    return render(request, login_url, context)




def logoutUser(request):
    logout(request)
    return redirect('login')

    
def about(request):
    return render(request, 'about.html',{})
