from django.urls import path
from .views import CreateChargeView

urlpatterns = [
    path('', CreateChargeView.as_view(), name='pay'),
]
