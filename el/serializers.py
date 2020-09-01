from rest_framework import serializers
from .models import ExtractLossData

class ExtractLossDataSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    shift = serializers.CharField(source='shift.shift_name')
    product = serializers.CharField(source='product.product_name')

    class Meta:
        model = ExtractLossData
        fields = '__all__'
