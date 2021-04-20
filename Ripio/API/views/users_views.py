from rest_framework import viewsets
from API.serializers.users_serializers import UserSerializer



class UsersViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
    