from django.urls import path
from .views import LanguageView

urlpatterns = [
    path('', LanguageView.as_view(), name='languages')
]

