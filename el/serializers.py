from rest_framework import serializers
from django.db.models import Sum
from trackel.products.models import Product
from trackel.shifts.models import Shift
from trackel.utils.custom_serializer_fields import MonthField, ShiftField
from .models import ExtractLossData

class ExtractLossDataSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    month = MonthField(read_only=True)
    week = serializers.IntegerField(read_only=True)
    class Meta:
        model = ExtractLossData
        fields = '__all__'

class ElByProductWeekSummary(serializers.Serializer):
    date = serializers.SerializerMethodField()
    week = serializers.SerializerMethodField()
    el = serializers.SerializerMethodField()
    week__count = serializers.IntegerField()

    def get_week(self, instance):
        return instance['week']

    def get_date(self, instance):
        w = instance['week']
        q = ExtractLossData.objects.filter(date__week=w).order_by('-date')[0]
        return q.date

    def get_el(self, instance):
        w = instance['week']
        q = ExtractLossData.objects.filter(date__week=w).aggregate(total=Sum('extract_loss_packaging'))
        return q['total']

class ElByProductMonthSummary(serializers.Serializer):
    date = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    el = serializers.SerializerMethodField()
    extract_loss_packaging__count = serializers.IntegerField()

    def get_month(self, instance):
        return instance['month']

    def get_date(self, instance):
        m = instance['month']
        q = ExtractLossData.objects.filter(date__month=m).order_by('-date')[0]
        return q.date

    def get_el(self, instance):
        m = instance['month']
        q = ExtractLossData.objects.filter(date__month=m).aggregate(total=Sum('extract_loss_packaging'))
        return q['total']
