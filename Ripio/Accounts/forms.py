from django import forms
from django.forms import ValidationError
from .models import Account
from Users.models import User
from Currencies.models import Currency


#############################################[  GLOBALS  ]############################################
ACCOUNT_NUMBER = 'Ya existe una cuenta con el mismo numero  registrada en nuestro sistema '
ALIAS_EQUAL = 'Ya existe este alias registrado en nuestro sistema'
BALANCE_VALUE = 'No puede crear una cuenta sin dinero , por favor solicite monedas en nuestra seccion de compras'
##############################################[  MAIN  ]##############################################



class AccountForm(forms.ModelForm):
    #Form to register a new Account in a database
    account_number = forms.CharField(label="Numero de cuenta", widget = forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Numero de cuenta ',
            'id':'account_number',
            'required':'required'
        }
    ))
    alias = forms.CharField(label="Alias", widget = forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Alias ',
            'id':'alias',
            'required':'required'
        }
    ))
    balance = forms.IntegerField(label="Saldo")
    class Meta:
        model = Account
        fields = ('account_number','alias','type_currency','balance','username')
        widget = {
        'account_number':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Numero de cuenta',
                }
            )},
        {
        'alias':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'alias',
                }
            )},
        {
        'balance':forms.FloatField()
        },
        {
        'username':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Usuario',
                }
            )},
        
    #Filter by user login
    def __init__(self, *args, **kwargs):
           user = kwargs.pop('username')
           super(AccountForm, self).__init__(*args, **kwargs)
           self.fields['username'].queryset = User.objects.filter(username=user)
           
    #Validations
    def clean_account_number(self,*args,**kwargs):
        #Is this account already in out system?
        account_number= self.cleaned_data.get('account_number')
        list_accounts = Account.objects.all()
        for accounts in list_accounts:
            if account_number == accounts.account_number:
                raise forms.ValidationError(ACCOUNT_NUMBER)
            else:
                return account_number
               
    def clean_alias(self,*args,**kwargs):
        #is this alias already in our system?
        alias= self.cleaned_data.get('alias')
        list_accounts = Account.objects.all()
        for accounts in list_accounts:
            if alias == accounts.alias:
                raise forms.ValidationError(ALIAS_EQUAL)
            else:
                return alias
    def clean_balance(self,*args,**kwargs):
        #is the balance less than 0?
        balance= self.cleaned_data.get('balance')
        if balance <= 0 :
            raise forms.ValidationError(BALANCE_VALUE)
        else:
            return balance