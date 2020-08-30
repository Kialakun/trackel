from rest_framework import serializers
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    class Meta:
        model = Shift
        fields = '__all__'
