from django import forms
from .models import Currency

#############################################[  GLOBALS  ]############################################
CURRENCY_NAME = 'Ya existe una moneda con este nombre registrada en nuestro sistema '
AMOUNT_VALUE = 'No puede crear una moneda con un monto de 0'
##############################################[  MAIN  ]##############################################



class CurrencyForm(forms.ModelForm):
    #FORM TO REGISTER A NEW CURRENCY IN A DATABASE 
    name = forms.CharField(label="Nombre", widget = forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Nombre ',
            'id':'name',
            'required':'required'
        }
    ))
    amount = forms.IntegerField(label="Monto")

    class Meta:
        model = Currency
        fields = ('name','image','amount','price')
        widget = {
        'image':forms.ImageField()
        },
        
        {
        'amount':forms.IntegerField()
        },
        {
        'price':forms.FloatField()
        } 
    #VALIDATE FOR THE AMOUNT MUST BE > 0
    def clean_amount(self,*args,**kwargs):
        amount = self.cleaned_data.get('amount')
        if int(amount)<= 0:
                raise forms.ValidationError(AMOUNT_VALUE)
        else:
            return amount