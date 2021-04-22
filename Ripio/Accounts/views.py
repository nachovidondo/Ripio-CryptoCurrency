from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Account
from .forms import  AccountForm


class AccountsBalance(ListView):
    model = Account
    template_name = 'accounts_balance.html'
    context_object_name = 'accounts'
    def get_queryset(self):
        #FILTER BY USER LOGIN
        queryset = Account.objects.filter(username=self.request.user)
        return queryset


class CreateAccount(CreateView):
    model = Account
    template_name = 'create_account.html'
    form_class =  AccountForm
    success_url = reverse_lazy('index')
    def get_form_kwargs(self):
        #FILTER BY USER LOGIN
        kwargs = super(CreateAccount, self).get_form_kwargs()
        kwargs['username'] = self.request.user
        return kwargs
    def get_queryset(self):
        currency = Account.objects.filter(username=user)