from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='dash_home'),
    path('products/', views.products_list, name='dash_products'),
    path('products/new/', views.product_create, name='dash_product_new'),
    path('products/<int:pk>/edit/', views.product_edit, name='dash_product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='dash_product_delete'),
    path('orders/', views.orders_list, name='dash_orders'),
    path('orders/<int:pk>/', views.order_detail, name='dash_order_detail'),
]
