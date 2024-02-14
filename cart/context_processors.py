from .cart import Cart

# create the context processor for it to work everywhere

def cart(request):
    # return default data from cart
    return {'cart': Cart(request)}
