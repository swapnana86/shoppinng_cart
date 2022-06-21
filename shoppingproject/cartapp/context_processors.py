# For counting Items
from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    print('counter func called' + request.path)
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            print(cart)
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            print('ffffffffffffffffffffffffffffffffitemcount empty')
            item_count = 0
    return dict(item_count=item_count)
