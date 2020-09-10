from django.db.models import Sum, Avg
from rest_framework import serializers
from trackel.el.models import ExtractLossData
from trackel.utils.custom_serializer_fields import ProductField, ExtractLossDataField, MonthField
from .models import Heuft1, Heuft2
from trackel.products.models import Product

class Heuft1Serializer(serializers.ModelSerializer):
    """Heuft1 serializer"""
    product = ProductField(queryset=Product.objects.all())

    class Meta:
        model = Heuft1
        fields = '__all__'
        read_only_fields = ['total_loss']

class Heuft2Serializer(serializers.ModelSerializer):
    """Heuft 2 Serializer"""
    product = ProductField(queryset=Product.objects.all())

    class Meta:
        model = Heuft2
        fields = '__all__'
        read_only_fields = ['total_loss']
