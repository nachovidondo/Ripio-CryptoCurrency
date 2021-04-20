from rest_framework import generics
from apps.api.serializers.user_serializers import UserSerializer



class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
    