from rest_framework import serializers
from trackel.el.models import ExtractLossData
from trackel.utils.custom_serializer_fields import ProductField, ExtractLossDataField
from .models import LossDeployment
from trackel.products.models import Product

class LossDeploymentSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    extract_loss_record = ExtractLossDataField(queryset=ExtractLossData.objects.all())
    product = ProductField(queryset=Product.objects.all())

    class Meta:
        model = LossDeployment
        fields = '__all__'

class LossDeploymentSummarySerializer(serializers.Serializer):
    """Loss deployment summary serializer takes a querset and returns summary"""
    heuft_1_rejects_total = serializers.DecimalField(max_digits=3, decimal_places=2)
    heuft_2_rejects_total = serializers.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        fields = ['heuft_1_rejects_total', 'heuft_2_rejects_total']
