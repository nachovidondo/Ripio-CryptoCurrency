from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from API.serializers.currency_serializers import CurrencySerializer



class CurrencyList(generics.ListCreateAPIView):
    serializer_class = CurrencySerializer
    queryset = CurrencySerializer.Meta.model.objects.all()
    #function overwritten-> personal message
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Mensaje':'Elemento creado correctamente!'},
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
    
    