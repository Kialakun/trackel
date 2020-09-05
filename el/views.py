import datetime
import calendar
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, F, Count
from rest_framework import viewsets, generics
from rest_framework import permissions
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from .serializers import ExtractLossDataSerializer, ElByProductMonthSummary, ElByProductWeekSummary
from .models import ExtractLossData
from trackel.products.models import Product
# Create your views here.
class ElByProductMonthSummary(generics.ListAPIView):
    serializer_class = ElByProductMonthSummary
    queryset = ExtractLossData.objects.values('month').annotate(Count('extract_loss_packaging'))
    permission_classes = [permissions.IsAuthenticated, ]

class ElByProductWeekSummary(generics.ListAPIView):
    serializer_class = ElByProductWeekSummary
    queryset = ExtractLossData.objects.values('week').annotate(Count('week'))
    permission_classes = [permissions.IsAuthenticated, ]

class ExtractLossDataViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ExtractLossDataSerializer
    queryset = ExtractLossData.objects.all().order_by('-date')
    permission_classes = [permissions.IsAuthenticated, ]

class ExtractLossDataExportViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ExtractLossDataSerializer
    queryset = ExtractLossData.objects.all().order_by('-date')
    permission_classes = [permissions.IsAuthenticated, ]
    renderer_classes = [XLSXRenderer,]
    file_name = 'extractlossdata.xlsx'

def test_view(request):
    queryset = ExtractLossData.objects.values('month').annotate(Count('month'))
    data = {
        'q': list(queryset)
    }
    return JsonResponse(data=data)

def weekly_summary_view(request):
    """API for dashboard charts"""

    data = {
        "data" : summary,
    }
    return JsonResponse(data=data)
