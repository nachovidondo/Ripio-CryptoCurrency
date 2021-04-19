from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from Currencies.models import Currency
from Accounts.models import Account



class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    origin_account = models.ForeignKey(
        Account, on_delete=models.CASCADE,
        verbose_name="Cuenta de origen"
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
    
#Signal to control User Currency amount
@receiver(post_save, sender=Transfer)
def transfer_save_detail(sender, instance, **kwargs):
    origin_account= instance.origin_account
    destination_account = instance.destination_account
    amount = instance.amount
    currency = instance.currency
    account_destination = Account.objects.get(account_number=destination_account)
    if origin_account:
        discount = int(origin_account.balance) - int(amount)
        origin_account.balance=discount
        origin_account.save()
    if account_destination:
        increase = int(account_destination.balance) + int(amount)
        account_destination.balance = increase
        account_destination.save()