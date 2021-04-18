from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CurrencyForm
from .models import Currency


class CurrenciesPriceList(ListView):
    model = Currency
    template_name = "currencies_price.html"

class ListCurrencies(ListView):
    model = Currency
    template_name = 'list_currencies.html'

class EditCurrency(UpdateView):
    model = Currency
    template_name = 'edit_currency.html'
    
    
class NewCurrency(CreateView):
    model = Currency
    template_name = 'new_currency.html'
    form_class =  CurrencyForm
    