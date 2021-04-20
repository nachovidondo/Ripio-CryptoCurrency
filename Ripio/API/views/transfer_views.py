from rest_framework import generics
from API.serializers.transfer_serializers import TransferSerializer



class TransferList(generics.ListCreateAPIView):
    serializer_class = TransferSerializer
    queryset = TransferSerializer.Meta.model.objects.all()
    
    