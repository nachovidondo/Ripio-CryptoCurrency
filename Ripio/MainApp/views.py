from django.shortcuts import render
from django.views.generic import ListView
from Currencies.models import Currency

class Index(ListView):
    model = Currency
    template_name = 'index.html'
    def get_queryset(self):
        currency = Currency.objects.all()
        return currency
   




    