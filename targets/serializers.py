from rest_framework import serializers
from .models import Target

class TargetSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    class Meta:
        model = Target
        fields = '__all__'
