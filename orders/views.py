from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .cart import Cart
from .forms import CheckoutForm
from .models import Order, OrderItem
def cart_detail(request):
    return render(request, 'orders/cart.html', {'cart': Cart(request)})
def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    qty = int(request.POST.get('quantity', 1)) if request.method == 'POST' else 1
    Cart(request).add(product, quantity=qty)
    messages.success(request, f'Added {product.name} to cart.')
    return redirect(request.POST.get('next') or 'cart_detail')
def cart_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    Cart(request).remove(product)
    return redirect('cart_detail')
def cart_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    qty = int(request.POST.get('quantity', 1))
    Cart(request).add(product, quantity=qty, override=True)
    return redirect('cart_detail')
@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.info(request, 'Your cart is empty.')
        return redirect('product_list')
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.payment_method = 'cod'
            order.total = cart.total
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'], name=item['name'],
                    price=item['price'], quantity=item['quantity'],
                )
                if item['product']:
                    item['product'].stock = max(0, item['product'].stock - item['quantity'])
                    item['product'].save()
            cart.clear()
            return redirect('order_success', pk=order.pk)
    else:
        form = CheckoutForm(initial={'full_name': request.user.get_full_name() or request.user.username})
    return render(request, 'orders/checkout.html', {'form': form, 'cart': cart})
@login_required
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/success.html', {'order': order})
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})
