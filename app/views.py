from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Test
from .serializers import TestSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
