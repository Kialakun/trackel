import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, F, Avg
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

class Heuft2ViewSet(viewsets.ModelViewSet):
    """Heuft 1 Model View Set"""
    def get_queryset(self, *args, **kwargs):
        """overriding queryset to include custom query params"""
        queryset = Heuft2.objects.all()
        # check query params
        # group by
        groupby = self.request.query_params.get('groupby', False)
        # get date
        date = self.request.query_params.get('date', None)
        if date:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
        # week summary or month summary
        unit = self.request.query_params.get('unit', None)
        # product
        product = self.request.query_params.get('product', None)
        # line
        line = self.request.query_params.get('line', None)

        # filter by line
        if line:
            queryset = queryset.filter(line=line)

        # filter by product
        if product:
            queryset = queryset.filter(product__product_code=product)

        # filter by month or week
        if unit == 'w':
            queryset = queryset.filter(date__week=date.isocalendar()[1])
            # group by
            if groupby:
                queryset = queryset.values('product__id'). \
                annotate(
                    total_loss=Sum('total_loss'),
                    date=F('date'),
                    product=F('product__product_code'),
                    line=F('line'),
                    canted_closure=Sum('canted_closure'),
                    leaking_pressure=Sum('leaking_pressure'),
                    low_fill=Sum('low_fill'),
                    uncrowned=Sum('uncrowned')
                    )

        elif unit == 'm':
            queryset = queryset.filter(date__month=date.month)
            # group by
            if groupby:
                queryset = queryset.values('product__id'). \
                annotate(
                    total_loss=Avg('total_loss'),
                    date=F('date'),
                    product=F('product__product_code'),
                    line=F('line'),
                    canted_closure=Avg('canted_closure'),
                    leaking_pressure=Avg('leaking_pressure'),
                    low_fill=Avg('low_fill'),
                    uncrowned=Avg('uncrowned')
                    )

        return queryset

    serializer_class = Heuft2Serializer
    permission_classes = [permissions.IsAuthenticated, ]

class Heuft1ViewSet(viewsets.ModelViewSet):
    """Heuft 1 Model View Set"""
    def get_queryset(self, *args, **kwargs):
        """overriding queryset to include custom query params"""
        queryset = Heuft1.objects.all()
        # check query params
        # group by
        groupby = self.request.query_params.get('groupby', False)
        # get date
        date = self.request.query_params.get('date', None)
        if date:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
        # week summary or month summary
        unit = self.request.query_params.get('unit', None)
        # product
        product = self.request.query_params.get('product', None)
        # line
        line = self.request.query_params.get('line', None)

        # filter by line
        if line:
            queryset = queryset.filter(line=line)

        # filter by product
        if product:
            queryset = queryset.filter(product__product_code=product)

        # filter by month or week
        if unit == 'w':
            queryset = queryset.filter(date__week=date.isocalendar()[1])
            # group by
            if groupby:
                queryset = queryset.values('product__id'). \
                annotate(
                    total_loss=Sum('total_loss'),
                    date=F('date'),
                    product=F('product__product_code'),
                    line=F('line'),
                    filling_tube=Sum('filling_tube'),
                    filling=Sum('filling'),
                    closure=Sum('closure')
                    )

        elif unit == 'm':
            queryset = queryset.filter(date__month=date.month)
            # group by
            if groupby:
                queryset = queryset.values('product__id'). \
                annotate(
                    total_loss=Avg('total_loss'),
                    date=F('date'),
                    product=F('product__product_code'),
                    line=F('line'),
                    filling_tube=Avg('filling_tube'),
                    filling=Avg('filling'),
                    closure=Avg('closure')
                    )

        return queryset

    serializer_class = Heuft1Serializer
    permission_classes = [permissions.IsAuthenticated, ]

# class Heuft1ExportViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
#     """View set for loss deployment exporting to .xlsx file"""
#     queryset = LossDeployment.objects.all()
#     serializer_class = LossDeploymentSerializer
#     permission_classes = [permissions.IsAuthenticated, ]
#     renderer_classes = (XLSXRenderer,)
#     filename = 'lossdeployment.xlsx'
