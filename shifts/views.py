from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ShiftSerializer
from .models import Shift
# Create your views here.

class ShiftViewSet(viewsets.ModelViewSet):
    """View set for Extract Loss Data"""
    serializer_class = ShiftSerializer
    queryset = Shift.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]
