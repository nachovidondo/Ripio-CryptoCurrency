from django import forms
from Accounts.models import Account
from Currencies.models import Currency
from .models import Transfer



#############################################[  GLOBALS  ]############################################
ACCOUNT_UNKOWN = 'La cuenta de destino no esta registrada en el sistema, por favor verifique si es correcta '
AMOUNT_VALUE = 'No puede transferir un monto menor o igual a 0'
AMOUNT_ACCOUNT = 'Su saldo es insuficiente para realizar esta transferencia'
CURRENCY_INVALID = 'Las cuentas solicitadas no poseen la moneda seleccionada'
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
           super(TransferForm, self).__init__(*args, **kwargs)
           self.fields['origin_account'].queryset = Account.objects.filter(username=user)
    #VALIDATIONS WITH ACCOUNTS - TYPE OF CURRENCY - AMOUNT 
    def clean(self):
        #INSTANCE OF FORM FIELDS
        data_origin_account = self.cleaned_data.get('origin_account')
        data_destination_account = self.cleaned_data.get('destination_account')
        data_currency = self.cleaned_data.get('currency')
        data_amount = self.cleaned_data.get('amount')
        origin_account = Account.objects.filter(account_number=data_origin_account).first()
        destination_account = Account.objects.filter(account_number=data_destination_account).first()
        
        if destination_account:
            if origin_account.type_currency != data_currency:
                raise forms.ValidationError(CURRENCY_INVALID)
            if destination_account.type_currency != data_currency:
                raise forms.ValidationError(CURRENCY_INVALID)
            if int(data_amount) > int(origin_account.balance):
                raise forms.ValidationError(AMOUNT_ACCOUNT)
            if int(data_amount)<= 0 :
                raise forms.ValidationError(AMOUNT_VALUE )
            return self.cleaned_data
        raise forms.ValidationError(ACCOUNT_UNKOWN)
   