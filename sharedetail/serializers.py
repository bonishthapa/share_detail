from rest_framework import serializers
from sharedetail.models import ShareBrought, ShareSold


class ShareBroughtSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShareBrought
        fields = ['id', 'name', 'quantity', 'brought_rate', 'brought_date', 'total_price']

class ShareSoldSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShareSold
        fields = ['id', 'name', 'quantity', 'brought_rate', 'brought_date', 'sold_rate', 'sold_date', 'brought_total_price', 'sold_total_price', 'profit_or_loss']
