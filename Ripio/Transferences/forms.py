from django import forms
from Accounts.models import Account
from .models import Transfer


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        #Function to filter all the accounts from the user login
           user = kwargs.pop('username')
           super(TransferForm, self).__init__(*args, **kwargs)
           self.fields['origin_account'].queryset = Account.objects.filter(username=user)