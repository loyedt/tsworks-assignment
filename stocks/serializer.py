from rest_framework import serializers
from .models import Stockval

class StockvalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stockval
        fields=('date','open','high','low','adj_close','volume')
