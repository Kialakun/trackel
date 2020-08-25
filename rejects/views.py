from django.shortcuts import render
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
