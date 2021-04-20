from rest_framework import generics
from apps.api.serializers.currency_serializers import CurrencySerializer


class CurrencyList(generics.ListCreateAPIView):
    serializer_class = CurrencySerializer
    queryset = CurrencySerializer.Meta.model.objects.all()
    
    