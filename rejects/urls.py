from django.urls import path
from . import views

urlpatterns = [
    path('api/rejectsmonthsummary', views.LossDeploymentMonthSummaryListAPIView.as_view(), name='RejectsMonthSummary'),
    #path('api/rejectsweeksummary', views.week_summary_view, name='RejectsWeekSummary'),

]
