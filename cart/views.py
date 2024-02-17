from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.contrib import messages
from store.models import Product
from django.http import JsonResponse
# Create your views here.

def cart_sum(request):
    # get Cart
    cart = Cart(request)
    cart_products = cart.get_prod
    quantities = cart.get_quantity
    total = cart.cart_total

    return render(request, 'cart_sum.html', {"cart_products": cart_products, 'quantities': quantities, 'total':total})

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = request.POST.get('product_id')

        # delete funtion
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        messages.success(request, ("Item deleted from cart"))
        return response
    

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')

        cart.update(product=product_id, quantity=product_quantity)

        response = JsonResponse({'Quantity': product_quantity})
        messages.success(request, ("Your cart has been updated"))
        return response





def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        # get stuff
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')

        # find the product
        product = get_object_or_404(Product, id=product_id)

        # store in settion 
        cart.add(product=product, quantity=product_quantity)

        # get quantity number
        cart_quantity = cart.__len__()

        # return response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'Quantity: ': cart_quantity})
        messages.success(request, ("Product added to cart"))
        return response
