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
    month = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    def get_month(self, instance):
        return instance['month']

    def get_value(self, instance):
        q = ExtractLossData.objects.filter(date__month=instance['month'])
