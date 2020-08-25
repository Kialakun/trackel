from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    class Meta:
        model = Product
        fields = '__all__'
