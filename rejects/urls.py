from django.urls import path
from . import views

urlpatterns = [
    path('api/rejectsmonthsummary', views.month_summary_view, name='RejectsMonthSummary'),
    path('api/rejectsweeksummary', views.week_summary_view, name='RejectsWeekSummary'),

]
