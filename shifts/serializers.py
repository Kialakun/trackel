from rest_framework import serializers
from trackel.utils.custom_serializer_fields import SupervisorField
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    shift_supervisor = SupervisorField()

    class Meta:
        model = Shift
        fields = '__all__'
