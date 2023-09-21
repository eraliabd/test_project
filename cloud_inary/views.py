from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Language
from .serializers import LanguageSerializer


class LanguageView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

