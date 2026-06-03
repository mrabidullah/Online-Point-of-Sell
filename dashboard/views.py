from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.contrib import messages
from products.models import Product, Category
from orders.models import Order, STATUS_CHOICES
from .forms import ProductForm

staff_required = user_passes_test(lambda u: u.is_active and u.is_staff)

@login_required
@staff_required
def home(request):
    stats = {
        'orders': Order.objects.count(),
        'pending': Order.objects.filter(status='pending').count(),
        'revenue': Order.objects.filter(status__in=['confirmed','shipped','delivered']).aggregate(s=Sum('total'))['s'] or 0,
        'products': Product.objects.count(),
    }
    recent = Order.objects.order_by('-created_at')[:8]
    return render(request, 'dashboard/home.html', {'stats': stats, 'recent': recent})

@login_required
@staff_required
def products_list(request):
    return render(request, 'dashboard/products.html', {'products': Product.objects.all().order_by('-created_at')})

@login_required
@staff_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product created.')
        return redirect('dash_products')
    return render(request, 'dashboard/product_form.html', {'form': form, 'title': 'New product'})

@login_required
@staff_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product updated.')
        return redirect('dash_products')
    return render(request, 'dashboard/product_form.html', {'form': form, 'title': f'Edit {product.name}'})

@login_required
@staff_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted.')
        return redirect('dash_products')
    return render(request, 'dashboard/confirm_delete.html', {'object': product})

@login_required
@staff_required
def orders_list(request):
    status = request.GET.get('status', '')
    orders = Order.objects.all().order_by('-created_at')
    if status:
        orders = orders.filter(status=status)
    return render(request, 'dashboard/orders.html', {'orders': orders, 'statuses': STATUS_CHOICES, 'active': status})

@login_required
@staff_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, 'Status updated.')
            return redirect('dash_order_detail', pk=pk)
    return render(request, 'dashboard/order_detail.html', {'order': order, 'statuses': STATUS_CHOICES})
