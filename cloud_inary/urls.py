from django.urls import path
from .views import LanguageView

urlpatterns = [
    path('languages/', LanguageView.as_view(), name='languages')
]

