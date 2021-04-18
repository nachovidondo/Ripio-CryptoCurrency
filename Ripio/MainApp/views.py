from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from Users.models import User

def index(request):
    user = User.objects.filter(username=request.user)
    print(user)
    return render(request, 'index.html')


    