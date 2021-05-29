from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ShareBroughtAPIVIew, ShareSoldAPIVIew

router = DefaultRouter()

router.register('sharebrought', ShareBroughtAPIVIew, basename='share-brought')
router.register('sharesold', ShareSoldAPIVIew, basename='share-sold')

urlpatterns = [
    path('api/', include(router.urls)),
]