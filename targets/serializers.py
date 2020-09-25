from rest_framework import serializers
from .models import Target

class TargetSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Target
        fields = '__all__'
