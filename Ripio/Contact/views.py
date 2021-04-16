from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']
        #Send Email
        send_mail(
            name,   
            message, 
            email,     #from email  
            ['ripiocurrencies@gmail.com'], #to email
            )
        print("ok")
        return render(request,'contact.html',{'name': name })
    else:
        return render(request, 'contact.html',{})