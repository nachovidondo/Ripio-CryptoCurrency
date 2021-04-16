from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import UserForm
from django.urls import reverse_lazy


class UserRegister(CreateView):
    model = User
    form_class = UserForm
    template_name = "Users/register.html"
    success_url = reverse_lazy('register')
