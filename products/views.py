from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
