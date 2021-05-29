from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserAPIView

router = DefaultRouter()

router.register('user', UserAPIView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]