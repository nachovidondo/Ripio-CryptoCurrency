from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ContactForm



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ripiocurrencies@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Mensaje no enviado ')
            return redirect('email_sent')
    return render(request, 'contact.html', {'form': form})


def email_sent(request):
    return render(request, 'email_sent.html')   