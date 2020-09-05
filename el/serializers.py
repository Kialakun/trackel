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

class ElByProductWeekSummary(serializers.Serializer):
    week = serializers.SerializerMethodField()
    el = serializers.SerializerMethodField()

    def get_week(self, instance):
        return instance['week']

    def get_el(self, instance):
        return instance['el']
