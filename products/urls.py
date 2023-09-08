from django.urls import path
from .views import ProductView, OrderView

urlpatterns = [
    path('products/', ProductView.as_view(), name='product'),
    path('orders/', OrderView.as_view(), name='order'),
]