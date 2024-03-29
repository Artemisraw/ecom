from django.shortcuts import render, redirect
from .models import Product
from .models import Category, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUser, ChangePass, UserInfo
from django import forms
from django.db.models import Q


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        if not searched:
            messages.success(request, "The Product Doesn't Exist - Please Try Again ")
            return render(request,'search.html', {})
        else:
            return render(request,'search.html', {'searched':searched})
    else:
        return render(request,'search.html', {})


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfo(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()

            messages.success(request, "User info has been Updated")
            return redirect('update_info')
        return render(request, "update_info.html", {'form': form})
       
    else:
        messages.success(request, "You must be logged in to access this page")
        return redirect('home')


def category_summary(request):
    categories = Category.objects.all()
    return render(request,'category_summary.html',{'categories':categories})

def category(request, cat):
    # replace space with hifen
    cat = cat.replace('-', ' ')

    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)

        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("Category doesnt exist"))
        return redirect('home')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html', {'product':product})

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'home.html', {'products':products})

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("you have logged in"))
            return redirect('home')
        else:
            messages.success(request, ("Invalid username or password "))
            return redirect('login')
    else:
        return render(request,'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            #login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Username Created - Please Fill Out Your User Info Below "))
            return redirect('home')
        else:
            messages.success(request, ("There was a problem while registering"))
            return redirect('register')
    else:
        return render(request,'register.html', {'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUser(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "User has been Updated")
            return redirect('home')
        return render(request, "update_user.html", {'user_form': user_form})
       
    else:
        messages.success(request, "You must be logged in to access this page")
        return redirect('login_user')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePass(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been updated.. ")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
             form = ChangePass(current_user)
             return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')

def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request,'register.html',context=mydict)

def payment_user(request):
    return render(request,'payment.html',{})