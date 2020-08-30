from django.urls import path

from . import views

# app_name = 'frontend'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('ExtractLoss/', views.el_view, name='el'),
]
