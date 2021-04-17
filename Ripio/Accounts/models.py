from django.db import models
from Users.models import User
from Currencies.models import Currency


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True,verbose_name="Estado de cuenta")
    account_number = models.CharField(
        max_length=200, verbose_name="Nº de cuenta", unique=True
        )
    alias = models.CharField(max_length=200,unique=True)
    type_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, verbose_name="Tipo de moneda"
        )
    balance = models.FloatField(verbose_name="Saldo")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuario"
        )
    creation_date = models.DateTimeField(auto_now=True, verbose_name="Fecha")
    
    class Meta:
        verbose_name="Cuenta"
        verbose_name_plural = "Cuentas"
    def __str__(self):
        return str(self.account_number)
    