from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Transfer
from django.views.generic import ListView ,View , CreateView
from Accounts.models import Account
from .forms import TransferForm


class AllTransferecesList(ListView):
    model = Transfer
    template_name = 'all_transferences.html'


class TransferecesList(ListView):
    model = Transfer
    template_name = 'my_transferences.html'
    def get_queryset(self):
        user = User.objects.filter(username=request.user)
        qs = Transfer.objects.filter(origin_account=user.account_number)
        return qs


class CreateTransfer(CreateView):
    model = Transfer
    template_name = 'create_transfer.html'
    form_class = TransferForm
    success_url = reverse_lazy('succesfull_transfer')


def transactions(request):
    return render(request, 'transactions.html')


def succesfull_transfer(request):
    return render(request, 'succesfull_transfer.html')