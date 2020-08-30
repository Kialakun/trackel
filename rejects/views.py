import datetime
from django.shortcuts import render
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LossDeploymentSerializer
from .models import LossDeployment
# Create your views here.

class LossDeploymentViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = LossDeploymentSerializer
    queryset = LossDeployment.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

class LossDeploymentMonthSummaryViewSet(viewsets.ModelViewSet):
    """View set loss deployment summary"""
    today = datetime.date.today()
    month = today.month
    serializer_class = LossDeploymentSerializer
    queryset = LossDeployment.objects.filter(shift__date__month=month).aggregate(pkg_filler_total=Sum('pkg_filler'), heuft_1_rejects_total=Sum('heuft_1_rejects'), heuft_2_rejects_total=Sum('heuft_2_rejects'))
    permission_classes = [permissions.IsAuthenticated, ]

class LossDeploymentYearSummaryViewSet(viewsets.ModelViewSet):
    """View set loss deployment summary"""
    today = datetime.date.today()
    year = today.year
    serializer_class = LossDeploymentSerializer
    queryset = LossDeployment.objects.filter(shift__date__year=year).aggregate(pkg_filler_total=Sum('pkg_filler'), heuft_1_rejects_total=Sum('heuft_1_rejects'), heuft_2_rejects_total=Sum('heuft_2_rejects'))
    permission_classes = [permissions.IsAuthenticated, ]
