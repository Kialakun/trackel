import datetime
import calendar
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
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
    def get_week_numbers(month, year):
        end_day = calendar.monthrange(year, month)[1] # get last day of month
        init_week = datetime.date(year, month, 1).isocalendar()[1]
        end_week = datetime.date(year, month, end_day).isocalendar()[1]
        return list(range(init_week, end_week + 1))

    today = datetime.date.today()
    m = today.month
    y = today.year

    weeks = get_week_numbers(m, y)

    summary = []
    for week in weeks:
        q = ExtractLossData.objects.filter(date__week=week).aggregate(total=Sum('extract_loss_packaging'))
        summary.append({week: q['total'] if q['total'] else 0})

    data = {
        "data" : summary,
    }
    return JsonResponse(data=data)
