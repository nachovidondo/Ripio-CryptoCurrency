from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CurrenciesPriceList



urlpatterns = [
    path('currencies_price', 
         login_required(CurrenciesPriceList.as_view()),
         name="currencies_price")
    ]