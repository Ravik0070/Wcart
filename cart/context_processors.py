from cart.carts import Cart

def cart(request):
    return{ 'cart':Cart(request)}