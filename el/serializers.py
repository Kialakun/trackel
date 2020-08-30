from rest_framework import serializers
from .models import ExtractLossData

class ExtractLossDataSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    shift = serializers.CharField(source='shift.shift_name')
    product = serializers.CharField(source='product.product_name')

    class Meta:
        model = ExtractLossData
        fields = '__all__'

class ExtractLossDataMonthSummarySerializer(serializers.Serializer):
    jan = serializers.SerializerMethodField()
    feb = serializers.SerializerMethodField()
    mar = serializers.SerializerMethodField()
    apr = serializers.SerializerMethodField()
    may = serializers.SerializerMethodField()
    jun = serializers.SerializerMethodField()
    jul = serializers.SerializerMethodField()
    aug = serializers.SerializerMethodField()
    sep = serializers.SerializerMethodField()
    oct = serializers.SerializerMethodField()
    nov = serializers.SerializerMethodField()
    dec = serializers.SerializerMethodField()

    def get_jan(self, instance)
