from django.urls import path
from .views import ProductView, ProductDetailView, OrderView, ProductListView, ProductsDetailView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    #######
    path('product/', ProductListView.as_view(), name='product'),
    path('product/<int:pk>/', ProductsDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('orders/', OrderView.as_view(), name='order'),
]
