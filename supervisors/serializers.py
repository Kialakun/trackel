from rest_framework import serializers
from .models import Supervisor

class SupervisorSerializer(serializers.ModelSerializer):
    """docstring for ExtractLossDataSerializer."""
    class Meta:
        model = Supervisor
        fields = '__all__'
