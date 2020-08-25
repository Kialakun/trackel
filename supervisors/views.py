from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import SupervisorSerializer
from .models import Supervisor
# Create your views here.

class SupervisorViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = SupervisorSerializer
    queryset = Supervisor.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
