from django.urls import path
from . import views

urlpatterns = [
    path('api/ElMonthSummary', views.monthly_summary_view, name='ElMonthSummary'),
    path('api/ElWeekSummary', views.ElByProductWeekSummary.as_view(), name='ElWeekSummary'),
]
