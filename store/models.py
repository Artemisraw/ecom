from django.db import models
import datetime
from django import forms

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    phone = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name =  models.CharField(max_length = 50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description =  models.CharField(max_length = 250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address =  models.CharField(default='', max_length=100,blank=True )
    phone =  models.CharField(max_length = 15,default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product


# Signup 
class SignUp(models.Model):
    Farmer = "f"
    Vendor = "v"
    Male = "m"
    Female = "f"

    User_Choices = (
        ('f', 'Farmer'),
        ('v', 'Vendor'),
    )

    Gender = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    Fname = models.CharField(max_length=40)
    Lname = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    gender = models.CharField(
        max_length=6, 
        choices=Gender,
        blank=True,
        default='m',
        help_text='Select Gender below',
    )
    user_type = models.CharField(
        max_length=6,
        choices=User_Choices,
        blank=True,
        default='f',
        help_text='Select Role below',
    )


class User(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = SignUp
        fields = ('Fname', 'Lname', 'email', 'password', 'number', 'gender', 'user_type')

    def clean(self):
        super(User.self).clean()
        number = self.cleaned_data.get('number')
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            self.errors['password'] = self.error_class(
                ['Password must be more than 8 characters']
            )
        if len(number) < 10:
            self.errors['number'] = self.error_class(
                ['Number is not valid, number is less than 10 characters']
            )
        if len(number) > 10:
            self.errors['number'] = self.error_class(
                ['Number is not valid, number is more than 10 characters']
            )    
        return self.cleaned_data

class Login(models.Model):
    password = forms.CharField(widget=forms.PasswordInput())

    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    