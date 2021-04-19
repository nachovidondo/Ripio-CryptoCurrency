from django.shortcuts import render
from django.views.generic import ListView
from django.core.mail import send_mail
from Users.models import User
from Currencies.models import Currency

class Index(ListView):
    model = Currency
    template_name = 'index.html'
    def get_queryset(self):
        #Login Send email
        user = User.objects.filter(email=self.request.user)
        
        """send_mail('Ripio nuevo ingreso a cuenta ', 
                  'Hola acabamos de registrar un ingreso a tu cuenta Ripio, si fuiste vos desestima este email. Es simpletemente una medida adicional de seguridad para que puedas monitorear los ingresos a tu cuenta . Si no fuiste vos , te pedimos que te comuniques con nosotros',
                  'ripiocurrencies@gmail.com', 
                   user,
                  fail_silently=False)"""
       
        currency = Currency.objects.all()
        return currency
   




    