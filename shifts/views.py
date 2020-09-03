from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from .serializers import ShiftSerializer
from .models import Shift
# Create your views here.

class ShiftViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ShiftSerializer
    queryset = Shift.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

class ShiftExportViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ShiftSerializer
    queryset = Shift.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    renderer_classes = [XLSXRenderer, ]
    file_name = 'shifts.xlsx'
