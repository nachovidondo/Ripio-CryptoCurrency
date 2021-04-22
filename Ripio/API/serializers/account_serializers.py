from rest_framework import serializers

from Accounts.models import Account



#############################################[  GLOBALS  ]############################################

INVALID_ACCOUNT_NUMBER = 'ESTE NUMERO DE CUENTA YA SE ENCUENTRA REGISTRADO EN EL SISTEMA'
INVALID_ALIAS = 'EL ALIAS PERTENECE A OTRA CUENTA DEL SISTEMA'
INVALID_CURRENCY = 'EL USUARIO YA TIENE CUENTAS REGISTRADAS CON EL MISMO TIPO DE MONEDAS '
##############################################[  MAIN  ]##############################################



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
    def to_representation(self, instance):
        return{
                 'id': instance.id,
                 'account_number': instance.account_number,
                 'alias': instance.alias,
                 'type_currency': instance.type_currency.name,
                 'balance':instance.balance,
                 'username': instance.username.name,
                 'creation_date': instance.creation_date,
                 }
    #VALIDATIONS 
    def validate_account_number(self,value):
        account_number = Account.objects.all()
        for account in account_number:
            if value != account.account_number :
                return value
            raise ValueError(INVALID_ACCOUNT_NUMBER)
        
    def validate_alias(self,value):
        account_alias = Account.objects.all()
        for account in account_alias:
            if value != account.alias:
                return value
            raise ValueError(INVALID_ALIAS)
        
    def validate_type_currency(self,value):
        data = self.get_initial()
        data_username = data.get('username')
        accounts= Account.objects.filter(type_currency=value)
        if accounts:
            for account in accounts:
                if int(account.username.id) == int(data_username):
                    raise ValueError(INVALID_CURRENCY)
        return value