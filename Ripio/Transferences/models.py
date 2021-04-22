from django.db import models
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from Currencies.models import Currency
from Accounts.models import Account
from Users.models import User



class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    origin_account = models.ForeignKey(
        Account, on_delete=models.CASCADE,verbose_name="Cuenta de origen"
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
    #INSTANCE OF FORM FIELDS
    origin_account= instance.origin_account
    destination_account = instance.destination_account
    amount = instance.amount
    currency = instance.currency
    #INSTANCE FOR DESTINATION ACCOUNT 
    account_destination = Account.objects.get(account_number=destination_account)
    #OPERATION BETWEEN USERS ACCOUNTS
    if origin_account:
        discount = int(origin_account.balance) - int(amount)
        origin_account.balance=discount
        origin_account.save()
    if account_destination:
        increase = int(account_destination.balance) + int(amount)
        account_destination.balance = increase
        account_destination.save()
   
    #SEND EMAIL TO THE USERS INVOLVED IN THE TRANSFER
    origin_user= User.objects.get(username=origin_account.username)
    destination_user = User.objects.get(username=account_destination.username)
    email_origin=origin_user.email
    email_destination = destination_user.email
    send_mail('Ripio nuevo transferencia generada', 
                  'Transferencia generada donde tu cuenta se encuentra involucrada. Aqui podras revisarla : http://127.0.0.1:8000/tranferences/ .. Muchas gracias',
                  'ripiocurrencies@gmail.com', 
                   [email_origin,email_destination],
                  fail_silently=False)
    
 

  
  