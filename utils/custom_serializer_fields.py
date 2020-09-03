from rest_framework import serializers
from trackel.supervisors.models import Supervisor

class SupervisorField(serializers.Field):
    """
    Color objects are serialized into 'rgb(#, #, #)' notation.
    """
    def to_representation(self, value):
        return value.__str__()

    def to_internal_value(self, data):
        name = data.split(' ')
        q = Supervisor.objects.filter(first_name=name[0]).filter(last_name=name[1])
        return q
