from rest_framework import serializers
from sharedetail.models import ShareBrought, ShareSold
from user.serializers import UserSerializer


class ShareBroughtSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ShareBrought
        fields = ['id', 'user', 'name', 'quantity', 'brought_rate', 'brought_date', 'total_price']


class ShareSoldSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ShareSold
        fields = ['id', 'user', 'name', 'quantity', 'brought_rate', 'brought_date', 'sold_rate', 'sold_date', 'brought_total_price', 'sold_total_price', 'profit_or_loss']
