from rest_framework import serializers
from trackel.supervisors.models import Supervisor
from trackel.el.models import ExtractLossData
from trackel.shifts.models import Shift
from trackel.products.models import Product

class SupervisorField(serializers.RelatedField):
    """
    Color objects are serialized into 'rgb(#, #, #)' notation.
    """
    def to_representation(self, value):
        return value.__str__()

    def to_internal_value(self, data):
        name = data.split(' ')
        q = Supervisor.objects.filter(first_name__contains=name[0]).filter(last_name__contains=name[1])
        return q

class ExtractLossDataField(serializers.RelatedField):
    """Extract Loss Data field"""
    def to_representation(self, value):
        return value.__str__()

    def to_internal_value(self, data):
        id = data.split(' | ')[0].split('-')[1]
        q = ExtractLossData.objects.filter(id=id)
        return q

class ProductField(serializers.RelatedField):
    """Product custom field"""
    def to_representation(self, instance):
        return instance.__str__()

    def to_internal_value(self, instance):
        name, packaging = instance.split(' | ')
        q = Product.objects.filter(product_name=name).filter(product_packaging=packaging)
        return q

class ShiftField(serializers.RelatedField):
    """Shift custom field"""
    def to_representation(self, instance):
        return instance.__str__()

    def to_internal_value(self, instance):
        name, supervisor = instance.split(' | ')
        q = Shift.objects.filter(shift_name=name).filter(shift_supervisor=supervisor)
        return q
