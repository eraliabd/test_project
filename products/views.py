from django.shortcuts import render
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.generics import ListCreateAPIView


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
