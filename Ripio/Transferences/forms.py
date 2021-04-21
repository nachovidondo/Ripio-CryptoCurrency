from django import forms
from Accounts.models import Account
from Currencies.models import Currency
from .models import Transfer



#############################################[  GLOBALS  ]############################################
ACCOUNT_UNKOWN = 'La cuenta de destino no esta registrada en el sistema, por favor verifique si es correcta '
AMOUNT_VALUE = 'No puede transferir un monto menor o igual a 0'
AMOUNT_ACCOUNT = 'Su saldo es insuficiente para realizar esta transferencia'
CURRENCY_INVALID = 'Las cuentas solicitadas no poseen la moneda seleccionada'
SECURITY_MESSAGE = 'Por razones de seguridad su transferencia ha sido invalida , comuniquese con nosotros'
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
           
    #VALIDATIONS 
    def clean(self):
        #INSTANCE OF FORM FIELDS
        total=0
        data_origin_account = self.cleaned_data.get('origin_account')
        data_destination_account = self.cleaned_data.get('destination_account')
        data_currency = self.cleaned_data.get('currency')
        data_amount = self.cleaned_data.get('amount')
        origin_account = Account.objects.filter(account_number=data_origin_account).first()
        destination_account = Account.objects.filter(account_number=data_destination_account).first()
          #VALIDATIONS BETWEEN ACCOUNTS - TYPE OF CURRENCY - AMOUNT 
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
    
'''     Validations to avoid double transaction :
        It is commented because it does not have control of the admin and 
        it would return error constantly, it should be have an automatical control with 
        paypal orderings.
        all_accounts = Account.objects.filter(type_currency=data_currency)
        for accounts in all_accounts:
                total += accounts.balance
                #All balance equal to currency amount
        if total != data_currency.amount:
        raise forms.ValidationError(SECURITY_MESSAGE)'''
        
       
   