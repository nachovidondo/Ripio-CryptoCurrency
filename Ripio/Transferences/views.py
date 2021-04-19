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
from .models import Transfer
from .forms import TransferForm
from Users.models import User


class AllTransferecesList(ListView):
    model = Transfer
    template_name = 'all_transferences.html'


class MyTransferences(ListView):
    model = Transfer
    template_name = 'my_transferences.html'
    
      


class CreateTransfer(CreateView):
    model = Transfer
    template_name = 'create_transfer.html'
    form_class = TransferForm
    success_url = reverse_lazy('succesfull_transfer')

    
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
            #response['Content-Disposition'] = 'attachment; filename= "transfer.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response)
            if pisaStatus.err:
                return HttpResponse('Han ocurrido algunos errores ')
            return response
         except:
            pass
         return HttpResponseRedirect(reverse_lazy('my_transferences'))

def transactions(request):
    return render(request, 'transactions.html')


def succesfull_transfer(request):
    return render(request, 'succesfull_transfer.html')