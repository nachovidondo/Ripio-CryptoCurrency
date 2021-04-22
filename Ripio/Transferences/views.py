import os
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from config.utils import render_to_pdf
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from django.views.generic import ListView ,View , CreateView, DetailView
from xhtml2pdf import pisa

from Accounts.models import Account
from Users.models import User
from .models import Transfer
from .forms import TransferForm



class AllTransferecesList(ListView):
    model = Transfer
    template_name = 'all_transferences.html'


class MyTransferences(ListView):
    model = Transfer
    template_name = 'my_transferences.html'
    def get_queryset(self):
        #QUERYSET TO FILTER BY USER LOGIN  TRANSFERENCES
        accounts = Account.objects.filter(username=self.request.user)
        if accounts:
            queryset = Transfer.objects.filter(origin_account__in=accounts)
            return queryset
        return None


class CreateTransfer(CreateView):
    model = Transfer
    template_name = 'create_transfer.html'
    form_class = TransferForm
    success_url = reverse_lazy('transactions')
    def get_form_kwargs(self):
        #FUNCTION TO FILTER ALL THE ACCOUNTS FROM THE USER LOGIN 
        kwargs = super(CreateTransfer, self).get_form_kwargs()
        kwargs['username'] = self.request.user
        return kwargs
    
    
class Download(DetailView):
    #PDF GENERATE
     def get(self, request,*args,**kwargs):
         try:
            template = get_template('download.html')
            context = {
                'transfer': Transfer.objects.get(pk=self.kwargs['pk'])
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisaStatus = pisa.CreatePDF(
                html, dest=response)
            if pisaStatus.err:
                return HttpResponse('Han ocurrido algunos errores ')
            return response
         except:
            pass
         return HttpResponseRedirect(reverse_lazy('my_transferences'))


def transactions(request):
    #SHOW THE MESSAGE ABOUT TRANSACTIONS CREATED
    return render(request, 'transactions.html')


