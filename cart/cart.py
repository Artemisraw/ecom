from store.models import Product, Order

class Cart():
    def __init__(self, request):
        self.session = request.session


        # Get current session
        cart = self.session.get('session_key')

        # if no session create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # make cart available everywhere
        self.cart = cart
    def add(self, product, quantity):
        product_id = str(product.id)
        product_quantity = str(quantity)

        #logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id]={'price': str(product.price)}
            self.cart[product_id]= int(product_quantity)
        
        self.session.modified = True
    
    # gives the length
    def __len__(self):
        return len(self.cart)

    
    def get_prod(self):
        # get ids from cart
        product_ids = self.cart.keys()

        # use id for the DB
        products = Product.objects.filter(id__in=product_ids)

        #return the products
        return products

    def get_quantity(self):
        quanties = self.cart
        return quanties

    def update(self, product, quantity):
        product_id = str(product)
        product_quantity = int(quantity)

        # get cart
        thecart = self.cart
        #update the dictionrary
        thecart[product_id] = product_quantity

        self.session.modified = True

        thing = self.cart

        return thing
    def delete(self, product):
        product_id = str(product)
        # delete from dictionary
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
    def cart_total(self):
        # get product id
        product_ids = self.cart.keys()

        # check keys with database
        products = Product.objects.filter(id__in=product_ids)

        # get quantities
        quanties = self.cart

        # Start totals
        total = 0
        for key, value in quanties.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)


        return total

        def order(self, product, quantity):
        product_id = str(product)
        product_quantity = int(quantity)


        order = Order.objects.get_or_create(product=product_id,quantity=product_quantity)

        # get cart
        thecart = self.cart
        #update the dictionrary
        thecart[product_id] = product_quantity

        self.session.modified = True

        thing = self.cart
