from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ShareBrought, ShareSold
from .serializers import ShareBroughtSerializer, ShareSoldSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ShareBroughtAPIVIew(viewsets.ModelViewSet):
    queryset = ShareBrought.objects.all()
    serializer_class = ShareBroughtSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)

    def create(self, request, **kwargs):
        if self.request.user.is_verified:
            serializer = ShareBroughtSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = ShareBroughtSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)


class ShareSoldAPIVIew(viewsets.ModelViewSet):
    queryset = ShareSold.objects.all()
    serializer_class = ShareSoldSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)

    def create(self, request, **kwargs):
        if self.request.user.is_verified:
            serializer = ShareSoldSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        if self.request.user.is_verified:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = ShareSoldSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)