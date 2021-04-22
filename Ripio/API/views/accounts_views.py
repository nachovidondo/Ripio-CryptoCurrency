from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from API.serializers.account_serializers import AccountSerializer



class AccountList(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = AccountSerializer.Meta.model.objects.all()
    #function overwritten-> personal message
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Mensaje':'Elemento creado correctamente!'},
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)


class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            account_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(account_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existe esta cuenta '},
                        status = status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            account_serializer = self.serializer_class(self.get_queryset(pk),
                                                       data = request.data)
            if account_serializer.is_valid():
                account_serializer.save()
                return Response(account_serializer.data, status = status.HTTP_100_CONTINUE)
            return Response(account_serializer.errors, status = status.HTTP_409_CONFLICT)
        
    def delete(self, request,pk=None):
        account = self.get_queryset().filter(id=pk).first()
        if account:
            account.delete()
            return Response({'Mensaje':'Cuenta eliminada correctamente'}, 
                            status = status.HTTP_200_OK)
        return Response({'error':'error al eliminar cuenta'}, 
                        status = status.HTTP_404_NOT_FOUND)