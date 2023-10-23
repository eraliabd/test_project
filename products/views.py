from django.views.generic import DetailView
from django.views import View
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render

from .models import Product, Order, Contact
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


####################### Django #######################################################
class ProductListView(View):  # ListView

    # queryset = Product.objects.all()
    # template_name = 'index.html'
    # context_object_name = 'products'

    def get(self, request):
        products = Product.objects.all()

        context = {
            "products": products
        }
        # print(context)
        return render(request, 'index.html', context=context)


class ProductsDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


################# Rest API #################################################
class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
