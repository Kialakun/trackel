from django.db.models import Sum
from rest_framework import serializers
from trackel.el.models import ExtractLossData
from trackel.utils.custom_serializer_fields import ProductField, ExtractLossDataField, MonthField
from .models import LossDeployment
from trackel.products.models import Product

class LossDeploymentSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    extract_loss_record = ExtractLossDataField(queryset=ExtractLossData.objects.all())
    product = ProductField(queryset=Product.objects.all())

    class Meta:
        model = LossDeployment
        fields = '__all__'

class LossDeploymentMonthSummarySerializer(serializers.Serializer):
    """Loss deployment summary serializer takes a querset and returns summary"""
    product = serializers.SerializerMethodField()
    m = MonthField()
    line = serializers.CharField()
    heuft_1_rejects_total = serializers.SerializerMethodField()
    heuft_2_rejects_total = serializers.SerializerMethodField()
    mcount = serializers.IntegerField()
    pcount = serializers.IntegerField()

    def get_product(self, instance):
        q = Product.objects.get(id=instance['product'])
        return q.__str__()

    def get_heuft_1_rejects_total(self, instance):
        m = instance['m']
        p = instance['product']
        q = LossDeployment.objects.filter(extract_loss_record__date__month=m). \
            filter(product__id=p). \
            aggregate(total=Sum('heuft_1_rejects'))
        return q['total']

    def get_heuft_2_rejects_total(self, instance):
        m = instance['m']
        q = LossDeployment.objects.filter(extract_loss_record__date__month=m).aggregate(total=Sum('heuft_2_rejects'))
        return q['total']

    class Meta:
        fields = ['product', 'heuft_1_rejects_total', 'heuft_2_rejects_total']
