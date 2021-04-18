from django import forms
from .models import Transfer

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'