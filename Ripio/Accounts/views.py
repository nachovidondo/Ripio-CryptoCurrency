from django.shortcuts import render
from django.views.generic import ListView
from .models import Account


class AccountsBalance(ListView):
    model = Account
    template_name = 'accounts_balance.html'
    context_object_name = 'accounts'
    queryset = Account.objects.filter(status=True)
    