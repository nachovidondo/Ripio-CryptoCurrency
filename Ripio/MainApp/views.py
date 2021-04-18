from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from Users.models import User

def index(request):

    return render(request, 'index.html')


    