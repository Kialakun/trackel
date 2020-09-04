from rest_framework import serializers
from trackel.shifts.models import Shift
from trackel.utils.custom_serializer_fields import SupervisorField
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    shift_supervisor = SupervisorField(queryset=Shift.objects.all())

    class Meta:
        model = Shift
        fields = '__all__'
