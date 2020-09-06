import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth, ExtractWeek
from django.http import Http404
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.response import Response
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from trackel.products.models import Product
from .serializers import LossDeploymentSerializer, LossDeploymentMonthSummarySerializer
from .models import LossDeployment
# Create your views here.
class LossDeploymentMonthSummaryListAPIView(generics.ListAPIView):
    serializer_class = LossDeploymentMonthSummarySerializer
    queryset = LossDeployment.objects. \
        annotate(m=ExtractMonth('extract_loss_record__date')). \
        values('m', 'product', 'line'). \
        annotate(mcount=Count('m'), pcount=Count('product'))
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        line = request.query_params.get('line')
        try:
            q = self.get_queryset()
            queryset = q.filter(line=line)
        except:
            raise Http404("Line does not exist.")

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
        q = LossDeployment.objects.filter(extract_loss_record__date__month=month
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
