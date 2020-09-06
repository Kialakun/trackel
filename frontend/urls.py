from django.urls import path

from . import views

# app_name = 'frontend'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('ExtractLoss/', views.el_view, name='el'),
    path('Supervisors/', views.supervisors_view, name='Supervisors'),
    path('Products/', views.products_view, name='Products'),
    path('Shifts/', views.shifts_view, name='Shifts'),
    path('LossDeployment/', views.lossdeployment_view, name='LossDeployment')
]
