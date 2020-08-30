from rest_framework import serializers
from .models import LossDeployment

class LossDeploymentSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    class Meta:
        model = LossDeployment
        fields = '__all__'

class LossDeploymentSummarySerializer(serializers.Serializer):
    """Loss deployment summary serializer takes a querset and returns summary"""
    pkg_filler_total = serializers.DecimalField(max_digits=3, decimal_places=2)
    heuft_1_rejects_total = serializers.DecimalField(max_digits=3, decimal_places=2)
    heuft_2_rejects_total = serializers.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        fields = ['pkg_filler_total', 'heuft_1_rejects_total', 'heuft_2_rejects_total']
