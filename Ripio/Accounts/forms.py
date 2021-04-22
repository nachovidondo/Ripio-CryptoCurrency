from django import forms
from django.forms import ValidationError
from .models import Account
from Users.models import User
from Currencies.models import Currency


#############################################[  GLOBALS  ]############################################
INVALID_ACCOUNT_NUMBER = 'ESTE NUMERO DE CUENTA YA SE ENCUENTRA REGISTRADO EN EL SISTEMA'
INVALID_ALIAS = 'EL ALIAS PERTENECE A OTRA CUENTA DEL SISTEMA'
INVALID_BALANCE_VALUE = 'Coloque 0 en el saldo de su cuenta , para comprar monedas solicite en nuestra seccion de compras '
##############################################[  MAIN  ]##############################################



class AccountForm(forms.ModelForm):
    #Form to register a new Account created in a database
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
        fields ='__all__'
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
        'balance':forms.IntegerField()
        },
        {
        'username':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Usuario',
                }
            )},
        
    
    def __init__(self, *args, **kwargs):
           #FILTER BY USER LOGIN
           user = kwargs.pop('username')
           super(AccountForm, self).__init__(*args, **kwargs)
           self.fields['username'].queryset = User.objects.filter(username=user)
     #VALIDATIONS
    def clean(self):
        #INSTANCE OF  THE FORM FIELDS
        data_account_number= self.cleaned_data.get('account_number')
        data_alias = self.cleaned_data.get('alias')
        data_balance = self.cleaned_data.get('balance')
        #VALIDATE FOR ACCOUNTS NUMBER AND ALIAS
        list_accounts = Account.objects.all()
        for accounts in list_accounts:
            if data_account_number == accounts.account_number:
                raise forms.ValidationError(INVALID_ACCOUNT_NUMBER)
            if data_alias == accounts.alias:
                 raise forms.ValidationError(INVALID_ALIAS)
         #BALANCE MUST BE 0
        if data_balance < 0 or data_balance > 0:
            raise forms.ValidationError(INVALID_BALANCE_VALUE)
        else:
            return self.cleaned_data
     