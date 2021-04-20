from rest_framework import serializers
from  Transferences.models import Transfer
from API.serializers.currency_serializers import CurrencySerializer
from API.serializers.account_serializers import AccountSerializer
from Currencies.models import Currency
from Accounts.models import Account

#############################################[  GLOBALS  ]############################################

INVALID_ORIGIN_ACCOUNT = 'CUENTA DE ORIGEN INVALIDA O NO REGISTRADA EN EL SISTEMA'
INVALID_DESTINATION_ACCOUNT = 'CUENTA DE DESTINO INVALIDA O NO REGISTRADA EN EL SISTEMA'
INVALID_RANGE = 'EL NUMERO INGRESADO ESTA FUERA DEL RANGO PERMITIDO'
INVALID_CURRENCY = 'EL TIPO DE MONEDA QUE DESEA TRANSFERIR ES INVALIDO PARA ESTAS CUENTAS'
INVALID_ACCOUNTS = 'LAS CUENTAS DE ORIGEN Y DESTINO NO PUEDEN SER IGUALES'

##############################################[  MAIN  ]##############################################

class TransferSerializer(serializers.ModelSerializer):
       class Meta:
              model = Transfer
              fields = '__all__'
        
       def to_representation(self, instance):
              return{
                 'id': instance.id,
                 'origin_account': instance.origin_account.account_number,
                 'destination_account': instance.destination_account,
                 'creation_date': instance.creation_date,
                 'currency': instance.currency.name,
                 'amount': instance.amount,
                 }
       #VALIDATIONS IN TRANSFER
       def validate_origin_account(self,value):
              account_origin = Account.objects.all()
              for account in account_origin:
                     if value == account.account_number:
                             return value
              raise serializers.ValidationError(INVALID_ORIGIN_ACCOUNT)
       
       def validate_destination_account(self,value):
              account_destination = Account.objects.all()
              print(value)
              for account in account_destination :
                     if value == account.account_number:
                            return value
              raise serializers.ValidationError(INVALID_DESTINATION_ACCOUNT)
       
       def validate_amount(self,value):
              if value > 0:
                     return value
              raise serializers.ValidationError(INVALID_RANGE)
       
       def validate_currency(self,value):
              data = self.get_initial()
              data_origin_account=data.get('origin_account')
              data_destination_account= data.get('destination_account')
              account_origin = Account.objects.get(account_number=data_origin_account)
              account_destination = Account.objects.get(account_number=data_destination_account)
              if value == account_origin.type_currency and value == account_destination.type_currency:
                     return value
              raise serializers.ValidationError(INVALID_CURRENCY)
       
       def validate(self,data):
              if data['origin_account'] == data['destination_account']:
                     raise serializers.ValidationError(INVALID_ACCOUNTS)
              return data