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
from .serializers import Heuft1Serializer, Heuft2Serializer
from .models import Heuft1, Heuft2
# Create your views here.
class Heuft1Summary(generics.ListAPIView):
    """api for viewing summarys"""
    serializer_class = Heuft1Serializer
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        """overriding list"""
        # check query params
        # get date
        date = request.query_params.get('date', None)
        if date:
            date = datetime.date(date)
        # week summary or month summary
        unit = request.query_params.get('unit', None)
        # product
        product = request.query_params.get('product', None)
        # line
        line = request.query_params.get('line', None)

        # get queryset
        queryset = self.get_queryset()

        # filter by month or week
        if unit == 'w':
            queryset = queryset.filter(date__week=date.isocalendar()[1])
        elif unit == 'm':
            queryset = queryset.filter(date___month=date.month)

        # filter by line
        if line:
            queryset = queryset.filter(line=line)

        # filter by product
        if product:
            queryset = queryset.filter(product__id=product)

class Heuft2ViewSet(viewsets.ModelViewSet):
    """Heuft 1 Model View Set"""
    queryset = Heuft2.objects.all()
    serializer_class = Heuft2Serializer
    permission_classes = [permissions.IsAuthenticated, ]

class Heuft1ViewSet(viewsets.ModelViewSet):
    """Heuft 1 Model View Set"""
    queryset = Heuft1.objects.all()
    serializer_class = Heuft1Serializer
    permission_classes = [permissions.IsAuthenticated, ]

# class Heuft1ExportViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
#     """View set for loss deployment exporting to .xlsx file"""
#     queryset = LossDeployment.objects.all()
#     serializer_class = LossDeploymentSerializer
#     permission_classes = [permissions.IsAuthenticated, ]
#     renderer_classes = (XLSXRenderer,)
#     filename = 'lossdeployment.xlsx'
