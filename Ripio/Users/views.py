from django.shortcuts import render, redirect
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
    
    def distpach(self,request,*args, **kwargs):
        #User Authenticated  -> index
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get.success_url())
             
        
        #Not User authenticated  -> Login again
        else:
            return super(Login,self).distpach(request,*args, **kwargs)
        
        def form_valid(self,form):
            #Validate if there is a user and login
            login(self.request,form.get_user())
            return super(Login,self).form_valid(form)
    

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class UserRegister(CreateView):
    model = User
    form_class = UserForm
    template_name = "register.html"
    
    def post(self,request,*args, **kwargs):
        # method to save password encrypted
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