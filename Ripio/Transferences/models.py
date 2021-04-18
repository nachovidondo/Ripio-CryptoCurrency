from django.db import models
from Currencies.models import Currency



class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    origin_account = models.CharField(
        max_length=200, verbose_name="Cuenta de origen"
        )
    destination_account = models.CharField(
        max_length=200,verbose_name="Cuenta de destino"
        )
    creation_date = models.DateTimeField(auto_now=True, verbose_name="Fecha")
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, verbose_name="Moneda"
        )
    amount = models.FloatField(verbose_name="Cantidad")
    
    class Meta:
        verbose_name="Transferencia"
        verbose_name_plural = "Transferencias"
        
    def __str__(self):
        return str(self.id)
