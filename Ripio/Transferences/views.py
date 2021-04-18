from django.shortcuts import render
from .models import Transfer
from django.views.generic import ListView
from Accounts.models import Account


class TransferecesList(ListView):
    model = Transfer
    template_name = 'all_transferences.html'
    

class TransferecesList(ListView):
    model = Transfer
    template_name = 'transferences.html'
    def get_queryset(self):
        user = Account.objects.get(username=self.request.user)
        print(self.request.user)
        qs = Transfer.objects.filter(origin_account=user)
        return qs
    