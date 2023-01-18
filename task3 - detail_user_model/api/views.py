from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User

from .serializers import UserSerializer
from .permissions import OzProfiliYaDaReadOnly, IsAdminOrReadOnly


# Create your views here.

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]



class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, OzProfiliYaDaReadOnly]
