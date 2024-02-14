from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.

def cart_sum(request):
    return render(request, 'cart_sum.html', {})

def cart_delete(request):
    pass

def cart_update(request):
    pass

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        # get stuff
        product_id = request.POST.get('product_id')

        # find the product
        product = get_object_or_404(Product, id=product_id)

        # store in settion 
        cart.add(product=product)

        # return response
        response = JsonResponse({'Product Name: ': product.name})
        return response
