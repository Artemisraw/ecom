from django.db import models
import datetime
from django import forms
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


# Create your models here.

# customer profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User,  auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=256, blank=True)
    address2 = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)



    def __str__(self):
        return self.user.username

    
    # default profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
# automate profile creation
post_save.connect(create_profile, sender=User)

class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length = 25)
    phone = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 256)
    password = models.CharField(max_length = 100)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, default=2)
    profile_pic = models.ImageField(upload_to='uploads/accounts/', null=True)

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



    