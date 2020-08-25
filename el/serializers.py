from rest_framework import serializers
from .models import ExtractLossData

class ExtractLossDataSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    class Meta:
        model = ExtractLossData
        fields = '__all__'
