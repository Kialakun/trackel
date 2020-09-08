from django.db.models import Sum, Avg
from rest_framework import serializers
from trackel.el.models import ExtractLossData
from trackel.utils.custom_serializer_fields import ProductField, ExtractLossDataField, MonthField
from .models import LossDeployment
from trackel.products.models import Product

class LdMonthSummaryByHeuftSerializer(serializers.Serializer):
    """Loss Deployment summary by heuft losses"""
    label = serializers.SerializerMethodField()
    product = serializers.CharField()
    canted_closure_total = serializers.DecimalField(max_digits=12, decimal_places=2)
    leaking_pressure_total = serializers.DecimalField(max_digits=12, decimal_places=2)
    low_fill_total = serializers.DecimalField(max_digits=12, decimal_places=2)
    uncrowned_total = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_losses = serializers.DecimalField(max_digits=12, decimal_places=2)

    def get_label(self, instance):
        return "Heuft 1"

class LossDeploymentSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    extract_loss_record = ExtractLossDataField(queryset=ExtractLossData.objects.all())
    product = ProductField(queryset=Product.objects.all())

    class Meta:
        model = LossDeployment
        fields = '__all__'
        read_only_fields = ['total_loss']

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
            aggregate(total=Avg('heuft_1_rejects'))
        return q['total']

    def get_heuft_2_rejects_total(self, instance):
        m = instance['m']
        p = instance['product']
        q = LossDeployment.objects.filter(extract_loss_record__date__month=m). \
            filter(product__id=p). \
            aggregate(total=Avg('heuft_2_rejects'))
        return q['total']

class LossDeploymentWeekSummarySerializer(serializers.Serializer):
    """Loss deployment summary serializer takes a querset and returns summary"""
    product = serializers.SerializerMethodField()
    w = serializers.IntegerField()
    line = serializers.CharField()
    heuft_1_rejects_total = serializers.SerializerMethodField()
    heuft_2_rejects_total = serializers.SerializerMethodField()
    mcount = serializers.IntegerField()
    pcount = serializers.IntegerField()

    def get_product(self, instance):
        q = Product.objects.get(id=instance['product'])
        return q.__str__()

    def get_heuft_1_rejects_total(self, instance):
        w = instance['w']
        p = instance['product']
        q = LossDeployment.objects.filter(extract_loss_record__date__week=w). \
            filter(product__id=p). \
            filter(heuft_number=1). \
            aggregate(total=Sum('total'))
        return q['total']

    def get_heuft_2_rejects_total(self, instance):
        w = instance['w']
        p = instance['product']
        q = LossDeployment.objects.filter(extract_loss_record__date__week=w). \
            filter(product__id=p). \
            filter(heuft_number=2). \
            aggregate(total=Sum('total'))
        return q['total']
