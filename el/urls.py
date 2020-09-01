from django.urls import path
from . import views

urlpatterns = [
    path('API/ElMonthlySummary', views.monthly_summary_view, name='elmonthlysummary-list'),
    path('API/ElWeeklySummary', views.weekly_summary_view, name='elweeklysummary-list'),
]
