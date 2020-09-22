import datetime
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Target
from .serializers import TargetSerializer
# Create your views here.

class TargetViewSet(viewsets.ModelViewSet):
    """Target Model ViewSet"""
    serializer_class = TargetSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self, *args, **kwargs):
        """get queryset based on query_params"""
        today = datetime.date.today()
        thisyear = today.year

        queryset = Target.objects.filter(timestamp__year=thisyear).order_by('-timestamp')
        return queryset
