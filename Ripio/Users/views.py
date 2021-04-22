from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import CreateView, View

from .models import User
from .forms import UserForm, LoginForm


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            #USER AUTHENTICATED -> INDEX
            return HttpResponseRedirect(self.get.success_url())
        #USER NOT AUTHENTICADED ->LOGIN AGAIN
        else:
            return super(Login,self).dispatch(request,*args, **kwargs)
    
    def form_valid(self,form):
        #SAVE THE USER
        login(self.request,form.get_user())
        #LOGIN SEND EMAIL TO THE USER
        user = User.objects.filter(username=self.request.user).first()
        email_user = user.email
        send_mail('Ripio nuevo ingreso a su cuenta', 
                  'Hola acabamos de registrar un ingreso a tu cuenta Ripio, si fuiste vos desestima este email. Es simpletemente una medida adicional de seguridad para que puedas monitorear los ingresos a tu cuenta . Si no fuiste vos , te pedimos que te comuniques con nosotros',
                  'ripiocurrencies@gmail.com', 
                   [email_user],
                  fail_silently=False)
        return super(Login,self).form_valid(form)
        


class UserRegister(CreateView):
    model = User
    form_class = UserForm
    template_name = 'register.html'
    
    def post(self,request,*args, **kwargs):
        # METHOD TO SAVE THE PASSWORD ENCRIPTED
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = User(
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                name = form.cleaned_data.get('name'),
                surname = form.cleaned_data.get('surname')
                )
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            return redirect('login')
        else:
            return render(request,self.template_name,{'form':form}) 


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
 
 