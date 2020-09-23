import datetime
import calendar
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, F, Count
from django.db.models.functions import ExtractMonth, ExtractWeek
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
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        """override get queryset"""
        # filter queryset to show only current years data
        today = datetime.date.today()
        thisyear = today.year

        queryset = ExtractLossData.objects.filter(date__year=thisyear)
        queryset = queryset.annotate(m=ExtractMonth('date')).values('m').annotate(count=Count('m')).order_by('-m')
        return queryset

class ElByProductWeekSummary(generics.ListAPIView):
    serializer_class = ElByProductWeekSummary
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        """override get queryset"""
        # filter queryset to show only current years data
        today = datetime.date.today()
        thisyear = today.year
        queryset = ExtractLossData.objects.filter(date__year=thisyear)
        queryset = queryset.annotate(w=ExtractWeek('date')).values('w').annotate(count=Count('w')).order_by('-w')
        return queryset

class ExtractLossDataViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ExtractLossDataSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        """override get queryset"""
        # filter queryset to show only current years data
        today = datetime.date.today()
        thisyear = today.year
        queryset = ExtractLossData.objects.filter(date__year=thisyear)
        queryset = queryset.order_by('-date')
        return queryset

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
