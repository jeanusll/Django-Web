from rest_framework import viewsets
from ..serializers.User_serializer import UserSerializer
from ..models.User import User

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()