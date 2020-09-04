from rest_framework import serializers
from trackel.products.models import Product
from trackel.shifts.models import Shift
from trackel.utils.custom_serializer_fields import ShiftField, ProductField
from .models import ExtractLossData

class ExtractLossDataSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""

    product = ProductField(queryset=Product.objects.all())

    class Meta:
        model = ExtractLossData
        fields = '__all__'

class ElByProductMonthSummary(serializers.Serializer):
    product = serializers.SerializerMethodField()
    el = serializer.SerializerMethodField()

    def get_product(self, instance):
        return instance.__str__()

    def get_el(self, instance):
        q = ExtractLossData.objects.filter(product__id=instance.id)
        return q
