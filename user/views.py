from django.shortcuts import render
from rest_framework import viewsets
from user.models import User
from user.serializers import UserSerializer
# Create your views here.


class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer