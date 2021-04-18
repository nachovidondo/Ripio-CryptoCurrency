from django.shortcuts import render
from django.views.generic import ListView
from .models import Currency


class CurrenciesPriceList(ListView):
    model = Currency
    template_name = "currencies_price.html"
    
