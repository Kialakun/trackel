from rest_framework import serializers
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    shift_supervisor = serializers.CharField(source='shift_supervisor.first_name')
    
    class Meta:
        model = Shift
        fields = '__all__'
