from django.shortcuts import render
from rest_framework import viewsets
from .models import ShareBrought, ShareSold
from .serializers import ShareBroughtSerializer, ShareSoldSerializer

# Create your views here.


class ShareBroughtAPIVIew(viewsets.ModelViewSet):
    queryset = ShareBrought.objects.all()
    serializer_class = ShareBroughtSerializer

class ShareSoldAPIVIew(viewsets.ModelViewSet):
    queryset = ShareSold.objects.all()
    serializer_class = ShareSoldSerializer