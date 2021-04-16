from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

#Custom Login Form
class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        
#Custom User Form
class UserForm(forms.ModelForm):
    #Form to register an User in a database
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required'
        }
    ))
    password2 = forms.CharField(label="Contraseña de confirmacion", widget = forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuveamente su contraseña',
            'id':'password2',
            'required':'required'
        }
    ))
    class Meta:
        model = User
        fields = ('email','username','name','surname')
        widget = {
        'email':forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Correo electronico',
                }
            )
        },
        {
        'name':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su nombre',
                }
            )
        }, 
        {
        'surname':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su apellido',
                }
            )
        },
        {
        'username':forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingrese su usuario',
                }
            )
        }, 
        def clean_password2(self):
            # Passwords Validation 
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if password1 != password2:
                raise forms.ValidationError('Las contraseñas no coinciden!')
            return password2
        
      
            