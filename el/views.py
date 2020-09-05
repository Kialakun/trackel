import datetime
import calendar
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, F
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
    queryset = ExtractLossData.objects.values('month').annotate(el=Sum('extract_loss_packaging'))
    permission_classes = [permissions.IsAuthenticated, ]

class ElByProductWeekSummary(generics.ListAPIView):
    serializer_class = ElByProductWeekSummary
    queryset = ExtractLossData.objects.values('week').annotate(el=Sum('extract_loss_packaging')).annotate(date=F('date'))
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

def monthly_summary_view(request):
    """API for dashboard charts"""
    MONTHS = (
        ('Jan', 1),
        ('Feb', 2),
        ('Mar', 3),
        ('Apr', 4),
        ('May', 5),
        ('Jun', 6),
        ('Jul', 7),
        ('Aug', 8),
        ('Sep', 9),
        ('Oct', 10),
        ('Nov', 11),
        ('Dec', 12),
    )

    labels = []
    datasets = [{
        'label':'Extract Loss',
        'data' : []
        }]

    for month in MONTHS:
        q = ExtractLossData.objects.filter(date__month=month[1]).aggregate(total=Sum('extract_loss_packaging'))
        labels.append(month[0])
        datasets[0]['data'].append(float(q['total']) if q['total'] else 0)

    data = {
        'data' : {
            'labels': labels,
            'datasets': datasets
        }
    }
    return JsonResponse(data=data)

def weekly_summary_view(request):
    """API for dashboard charts"""

    data = {
        "data" : summary,
    }
    return JsonResponse(data=data)
