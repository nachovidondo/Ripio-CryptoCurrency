from rest_framework import serializers

from Currencies.models import Currency



#############################################[  GLOBALS  ]############################################
CURRENCY_NAME = 'Ya existe una moneda con este nombre registrada en nuestro sistema '
AMOUNT_VALUE = 'No puede crear una moneda con un monto de 0'
##############################################[  MAIN  ]##############################################



class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
        
    def to_representation(self, instance):
        return{
            'name': instance.name,
            'amount': instance.amount,
            'price':instance.price,
               }
    #VALIDATIONS 
    def validate_name(self,value):
        currencies = Currency.objects.all()
        for currency in currencies:
            if value == currency.name :
                raise ValueError(CURRENCY_NAME)
            return value
        
    def validate_amount(self,value):
        if int(value)<= 0 :
            raise ValueError(AMOUNT_VALUE)
        return value
    
        