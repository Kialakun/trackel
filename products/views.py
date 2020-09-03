from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

class ProductExportViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    renderer_classes = [XLSXRenderer,]
    file_name = 'products.xlsx'
