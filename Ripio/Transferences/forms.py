from django import forms
from Accounts.models import Account
from .models import Transfer

#############################################[  GLOBALS  ]############################################
ACCOUNT_UNKOWN = 'La cuenta de destino no esta registrada en el sistema, por favor verifique si es correcta '
AMOUNT_VALUE = 'No puede transferir un monto menor a 0'
AMOUNT_ACCOUNT = 'Su saldo es insuficiente para realizar esta transferencia'
##############################################[  MAIN  ]##############################################

class TransferForm(forms.ModelForm):
    destination_account = forms.CharField(label="Cuenta de destino",
                                     widget=forms.TextInput(
                                         attrs={
                                             "placeholder":"Cuenta de destino"
                                         }
                                     ))
    amount = forms.CharField(label="Cantidad",
                                     widget=forms.TextInput(
                                         attrs={
                                             "placeholder":"Cantidad"
                                         }
                                     ))

    class Meta:
        model = Transfer
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        #Function to filter all the accounts from the user login
           user = kwargs.pop('username')
          
           account = Account.objects.filter(username=user)
           account_currency = account[0].type_currency.name
        
           super(TransferForm, self).__init__(*args, **kwargs)
           self.fields['origin_account'].queryset = Account.objects.filter(username=user)
           #self.fields ['currency'].queryset = Transfer.objects.filter(currency__name=account_currency)

          
           
    def clean_destination_account(self,*args,**kwargs):
        destination_account = self.cleaned_data.get('destination_account')
        accounts = Account.objects.filter(account_number=destination_account)
        if not accounts:
            raise forms.ValidationError(ACCOUNT_UNKOWN)
        else:
             return destination_account
    
    def clean_amount(self,*args,**kwargs):
        amount = self.cleaned_data.get('amount')
        origin_account = self.cleaned_data.get('origin_account')
        account = Account.objects.filter(account_number=origin_account)
        if int(amount)< 0:
            raise forms.ValidationError(AMOUNT_VALUE)
        if int(amount) > account[0].balance:
            raise forms.ValidationError(AMOUNT_ACCOUNT)
        else:
            return amount
    def clean_type_currency(self,*args,**kwargs):
        currency = self.cleaned_data.get('type_currency')
        print(currency)
        return currency
   
        

        