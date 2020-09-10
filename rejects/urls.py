from django.urls import path
from . import views

urlpatterns = [
    path('api/hueft1summary', views.Heuft1Summary.as_view(), name='Heuft1Summary'),
    #path('api/rejectsweeksummary', views.LossDeploymentWeekSummaryListAPIView.as_view(), name='RejectsWeekSummary'),
    #path('api/rejectsmonthsummarybyheuft', views.LdMonthSummaryByHeuftListAPIView.as_view(), name='RejectsMonthHeuftSummary'),
]
