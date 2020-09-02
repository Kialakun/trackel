import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework import permissions
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from trackel.products.models import Product
from .serializers import LossDeploymentSerializer
from .models import LossDeployment
# Create your views here.
@login_required
def week_summary_view(request):
    today = datetime.date.today()
    month = today.month

    labels = []
    datasets = [
        {
        'label':'Heuft 1 Rejects',
        'data' : []
        },
        {
        'label': 'Heuft 2 Rejects',
        'data': []
        }
    ]

    products = Product.objects.all()
    for product in products:
        q = LossDeployment.objects.filter(shift__date__month=month
            ).annotate(heuft_1_rejects_total=Sum('heuft_1_rejects')
            ).annotate(heuft_2_rejects_total=Sum('heuft_2_rejects'))

        labels.append(str(product))
        datasets[0]['data'].append(int(q[0].heuft_1_rejects_total if q[0].heuft_1_rejects_total else 0))
        datasets[1]['data'].append(int(q[0].heuft_2_rejects_total if q[0].heuft_2_rejects_total else 0))

    data = {
        'data' : {
            'labels': labels,
            'datasets' : datasets
        }
    }
    return JsonResponse(data=data)

@login_required
def month_summary_view(request):
    """summary for the month"""
    today = datetime.date.today()
    month = today.month

    products = Product.objects.all()

    labels = []
    datasets = [
        {
        'label':'Heuft 1 Rejects',
        'data' : []
        },
        {
        'label': 'Heuft 2 Rejects',
        'data': []
        }
    ]

    for product in products:
        q = LossDeployment.objects.filter(shift__date__month=month
            ).annotate(heuft_1_rejects_total=Sum('heuft_1_rejects')
            ).annotate(heuft_2_rejects_total=Sum('heuft_2_rejects'))

        labels.append(str(product))
        if q:
            datasets[0]['data'].append(float(q[0].heuft_1_rejects_total) if q[0].heuft_1_rejects_total else 0)
            datasets[1]['data'].append(float(q[0].heuft_2_rejects_total) if q[0].heuft_2_rejects_total else 0)
        else:
            datasets[0]['data'].append(0)
            datasets[1]['data'].append(0)

    data = {
        'data' : {
            'labels': labels,
            'datasets' : datasets
        }
    }
    return JsonResponse(data=data)

class LossDeploymentViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = LossDeploymentSerializer
    queryset = LossDeployment.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

class LossDeploymentExportViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    """View set for loss deployment exporting to .xlsx file"""
    queryset = LossDeployment.objects.all()
    serializer_class = LossDeploymentSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    renderer_classes = (XLSXRenderer,)
    filename = 'lossdeployment.xlsx'
