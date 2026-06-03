from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category
def product_list(request):
    q = request.GET.get('q', '').strip()
    cat = request.GET.get('category', '')
    products = Product.objects.filter(is_active=True)
    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
    if cat:
        products = products.filter(category__slug=cat)
    return render(request, 'store/product_list.html', {
        'products': products, 'categories': Category.objects.all(),
        'q': q, 'active_cat': cat,
    })
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'store/product_detail.html', {'product': product})
