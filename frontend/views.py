from django.shortcuts import render
from django.urls import reverse_lazy
from trackel.el.serializers import ExtractLossDataSerializer
from trackel.el.models import ExtractLossData
from trackel.products.serializers import ProductSerializer
from trackel.shifts.serializers import ShiftSerializer
from trackel.supervisors.serializers import SupervisorSerializer
from trackel.rejects.serializers import LossDeploymentSerializer
# Create your views here.
def lossdeployment_view(request):
    """Django view products_view"""
    context = {
        "page_title" : "Loss Deployment",
        "form" : LossDeploymentSerializer(),
        "url" : "lossdeployment-list",
        "export_url": "rejectsexport-list"
    }
    return render(request, 'datatables.html', context=context)

def products_view(request):
    """Django view products_view"""
    context = {
        "page_title" : "Products",
        "form" : ProductSerializer(),
        "url" : "product-list",
        "export_url": "productsexport-list"
    }
    return render(request, 'datatables.html', context=context)

def dashboard_view(request):
    """Django view dashboard"""
    context = {
        "page_title" : "Dashboard",
        "el_chart_url": "extractlossdata-list",
        "ld_chart_url": "lossdeployment-list"
    }
    return render(request, 'el_dashboard.html', context=context)

def el_view(request):
    """Django view el_view"""
    context = {
        "page_title" : "Extract Loss",
        "form" : ExtractLossDataSerializer(),
        "url" : "extractlossdata-list",
        "export_url" : "extractlossexport-list"
    }
    return render(request, 'datatables.html', context=context)

def supervisors_view(request):
    """Django view supervisors_views"""
    context = {
        "page_title" : "Supervisors",
        "form" : SupervisorSerializer(),
        "url" : "supervisor-list",
        "export_url" : "supervisorsexport-list"
    }
    return render(request, 'datatables.html', context=context)

def shifts_view(request):
    """Django view shifts_view"""
    context = {
        "page_title" : "Shifts",
        "form" : ShiftSerializer(),
        "url" : "shift-list",
        "export_url" : "shiftsexport-list"
    }
    return render(request, 'datatables.html', context=context)
