from django import forms
from .models import Account
from Users.models import User

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
           user = kwargs.pop('username')
           super(AccountForm, self).__init__(*args, **kwargs)
           self.fields['username'].queryset = User.objects.filter(username=user)