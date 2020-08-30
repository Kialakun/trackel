from django.shortcuts import render
from trackel.el.serializers import ExtractLossDataSerializer

# Create your views here.
def products_view(request):
    """Django view products_view"""
    context = {
        "page_title" : "Products",
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
        "form" : ExtractLossDataSerializer,
        "url" : "extractlossdata-list",
    }
    return render(request, 'datatables.html', context=context)

def supervisors_views(request):
    """Django view supervisors_views"""
    context = {
        "page_title" : "Supervisors",
    }
    return render(request, 'datatables.html', context=context)

def shifts_view(request):
    """Django view shifts_view"""
    context = {
        "page_title" : "Shifts",
    }
    return render(request, 'datatables.html', context=context)
