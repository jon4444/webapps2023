from django.urls import path
from .views import CurrencyConverterView

urlpatterns = [
    path('', CurrencyConverterView.as_view(), name='conversion'),
]
# /conversion/?base_currency=USD&target_currency=EUR&amount=100