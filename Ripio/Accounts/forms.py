from django import forms
from django.forms import ValidationError
from .models import Account
from Users.models import User
from Currencies.models import Currency



class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
    #Filter by user login
    def __init__(self, *args, **kwargs):
           user = kwargs.pop('username')
           super(AccountForm, self).__init__(*args, **kwargs)
           self.fields['username'].queryset = User.objects.filter(username=user)
           

    
   