from django.shortcuts import render
from .models import Transfer
from django.views.generic import ListView


class TransferecesList(ListView):
    model = Transfer
    template_name = 'transferences.html'
    

    