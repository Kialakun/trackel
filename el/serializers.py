from rest_framework import serializers
from .models import ExtractLossData

class ExtractLossDataSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    
    shift_name = serializers.CharField(source='shift.shift_name', read_only=True)
    product_name = serializers.CharField(source='product.product_name', read_only=True)

    class Meta:
        model = ExtractLossData
        fields = '__all__'
