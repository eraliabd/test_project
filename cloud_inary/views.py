from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Language
from .serializers import LanguageSerializer
from .pagination import CustomPagination


class LanguageView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    pagination_class = CustomPagination

