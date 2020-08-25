from rest_framework import serializers
from .models import LossDeployment

class LossDeploymentSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    class Meta:
        model = LossDeployment
        fields = '__all__'
