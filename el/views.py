from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ExtractLossDataSerializer
from .models import ExtractLossData
# Create your views here.

class ExtractLossDataViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ExtractLossDataSerializer
    queryset = ExtractLossData.objects.all().order_by('-date')
    permission_classes = [permissions.IsAuthenticated, ]
