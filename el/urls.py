from django.urls import path
from . import views

urlpatterns = [
    path('api/ElMonthSummary', views.ElByProductMonthSummary.as_view(), name='ElMonthSummary'),
    path('api/ElWeekSummary', views.ElByProductWeekSummary.as_view(), name='ElWeekSummary'),
    path('api/test', views.test_view, name='test'),
]
