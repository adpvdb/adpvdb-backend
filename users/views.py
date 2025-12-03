from rest_framework import generics

from .serializers import RegisterSerializer
from .models import User

class RegisterView(generic.CreateAPIView):
    queryset = USer.objects.all()
    serializer_class = RegisterSerializer


