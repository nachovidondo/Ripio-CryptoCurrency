from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Product, Order



def simpleCheckout(request):
	return render(request, 'base/simple_checkout.html')

def store(request):
    #LIST OF PRODUCTS
    products = Product.objects.all()
    return render(request, 'base/store.html',{'products': products})

def checkout(request, pk):
	product = Product.objects.get(id=pk)
	context = {'product':product}
	return render(request, 'base/checkout.html', context)

def paymentComplete(request):
    body = json.loads(request.body)
	return JsonResponse('Payment completed!', safe=False)