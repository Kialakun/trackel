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
from .serializers import LossDeploymentSerializer, LossDeploymentMonthSummarySerializer, LossDeploymentWeekSummarySerializer
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
        d = request.query_params.get('d', None)
        try:
            date = datetime.datetime.strptime(d, '%Y-%m-%d')
            m = date.month
        except:
            raise Http404("No date specified.")
        try:
            q = self.get_queryset()
            queryset = q.filter(line=line).filter(m=m)
        except:
            raise Http404("Line does not exist.")

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class LossDeploymentWeekSummaryListAPIView(generics.ListAPIView):
    serializer_class = LossDeploymentWeekSummarySerializer
    queryset = LossDeployment.objects. \
        annotate(w=ExtractWeek('extract_loss_record__date')). \
        values('w', 'product', 'line'). \
        annotate(mcount=Count('w'), pcount=Count('product'))
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        line = request.query_params.get('line')
        d = request.query_params.get('d', None)
        try:
            date = datetime.datetime.strptime(d, '%Y-%m-%d')
            w = date.isocalendar()[1]
        except:
            raise Http404("No date specified.")
        try:
            q = self.get_queryset()
            queryset = q.filter(line=line).filter(w=w)
        except:
            raise Http404("Line does not exist.")

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
