from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from .serializers import SupervisorSerializer
from .models import Supervisor
# Create your views here.

class SupervisorViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = SupervisorSerializer
    queryset = Supervisor.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

class SupervisorExportViewSet(XLSXFileMixin, viewsets.ReadOnlyModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = SupervisorSerializer
    queryset = Supervisor.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
    renderer_classes = [XLSXRenderer, ]
    file_name = 'supervisors.xlsx'
