from django import forms
from Accounts.models import Account
from .models import Transfer


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
           
    def clean_destination_account(self,*args,**kwargs):
        destination_account = self.cleaned_data.get('destination_account')
        accounts = Account.objects.filter(account_number=destination_account)
        if not accounts:
            raise forms.ValidationError('No se encuentra una cuenta como esta ')
        else:
             return destination_account
    
    def clean_amount(self,*args,**kwargs):
        amount = self.cleaned_data.get('amount')
        origin_account = self.cleaned_data.get('origin_account')
        currency = self.cleaned_data.get('type_currency')
        print(currency)
        account = Account.objects.filter(account_number=origin_account)
        if int(amount)< 0:
            raise forms.ValidationError('El monto transferido debe ser mayor a 0 ')
        if int(amount) > account[0].balance:
            raise forms.ValidationError('Saldo insuficiente en su cuenta ')
        else:
            return amount
            
            
        

        