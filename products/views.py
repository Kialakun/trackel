from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductaSerializer
from .models import Product
# Create your views here.

class ExtractLossDataViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
