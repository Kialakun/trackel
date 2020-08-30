"""trackel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

"""ViewSet Imports"""
from trackel.el.views import ExtractLossDataViewSet
from trackel.products.views import ProductViewSet
from trackel.shifts.views import ShiftViewSet
from trackel.rejects.views import LossDeploymentViewSet
from trackel.supervisors.views import SupervisorViewSet

router = DefaultRouter()

router.register(r'ExtractLoss', ExtractLossDataViewSet)
router.register(r'Products', ProductViewSet)
router.register(r'Shifts', ShiftViewSet)
router.register(r'Supervisors', SupervisorViewSet)
router.register(r'Rejects', LossDeploymentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('trackel.frontend.urls')),
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
]
