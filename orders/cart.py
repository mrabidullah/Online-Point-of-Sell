from decimal import Decimal
from products.models import Product
CART_SESSION_KEY = 'cart'
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_KEY)
        if not cart:
            cart = self.session[CART_SESSION_KEY] = {}
        self.cart = cart
    def add(self, product, quantity=1, override=False):
        pid = str(product.id)
        if pid not in self.cart:
            self.cart[pid] = {'quantity': 0, 'price': str(product.price), 'name': product.name}
        if override:
            self.cart[pid]['quantity'] = quantity
        else:
            self.cart[pid]['quantity'] += quantity
        if self.cart[pid]['quantity'] <= 0:
            self.remove(product)
        self.save()
    def remove(self, product):
        pid = str(product.id)
        if pid in self.cart:
            del self.cart[pid]
            self.save()
    def save(self):
        self.session[CART_SESSION_KEY] = self.cart
        self.session.modified = True
    def clear(self):
        self.session[CART_SESSION_KEY] = {}
        self.session.modified = True
    def __iter__(self):
        ids = self.cart.keys()
        products = {str(p.id): p for p in Product.objects.filter(id__in=ids)}
        for pid, item in self.cart.items():
            product = products.get(pid)
            yield {
                'product': product,
                'name': item['name'],
                'price': Decimal(item['price']),
                'quantity': item['quantity'],
                'subtotal': Decimal(item['price']) * item['quantity'],
            }
    def __len__(self):
        return sum(i['quantity'] for i in self.cart.values())
    @property
    def total(self):
        return sum(Decimal(i['price']) * i['quantity'] for i in self.cart.values())
