from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from trackel.el.serializers import ExtractLossDataSerializer
from trackel.el.models import ExtractLossData
from trackel.products.serializers import ProductSerializer
from trackel.shifts.serializers import ShiftSerializer
from trackel.supervisors.serializers import SupervisorSerializer
from trackel.rejects.serializers import Heuft1Serializer, Heuft2Serializer
from trackel.targets.serializers import TargetSerializer
# Create your views here.
def create_session(request):
    """create app session and show front page"""
    # Get token from auth
    token = request.headers.get('Authorization')
    # Create response object
    response = redirect('/accounts/login')
    # Set cookie based on token
    response.set_cookie(
        'ttid',
        value=token,
        max_age=1800, # 30 minutes
        secure=True,
        httponly=True,
        samesite='Lax'
    )
    return response


@login_required
def heuft2_view(request):
    """Django view products_view"""
    context = {
        "page_title" : "Heuft 2",
        "form" : Heuft2Serializer(),
        "url" : "heuft2-list",
        "export_url": "heuft2-list" # change
    }
    return render(request, 'datatables.html', context=context)

@login_required
def heuft1_view(request):
    """Django view products_view"""
    context = {
        "page_title" : "Heuft 1",
        "form" : Heuft1Serializer(),
        "url" : "heuft1-list",
        "export_url": "heuft1-list" # change
    }
    return render(request, 'datatables.html', context=context)

@login_required
def products_view(request):
    """Django view products_view"""
    context = {
        "page_title" : "Products",
        "form" : ProductSerializer(),
        "url" : "product-list",
        "export_url": "productsexport-list"
    }
    return render(request, 'datatables.html', context=context)

@login_required
def dashboard_view(request):
    """Django view dashboard"""
    context = {
        "page_title" : "Dashboard",
        "el_chart_url": "extractlossdata-list",
        "ld_chart_url": "lossdeployment-list"
    }
    return render(request, 'el_dashboard.html', context=context)

@login_required
def el_view(request):
    """Django view el_view"""
    context = {
        "page_title" : "Extract Loss",
        "form" : ExtractLossDataSerializer(),
        "url" : "extractlossdata-list",
        "export_url" : "extractlossexport-list"
    }
    return render(request, 'datatables.html', context=context)

@login_required
def targets_view(request):
    """Django view supervisors_views"""
    context = {
        "page_title" : "Targets",
        "form" : TargetSerializer(),
        "url" : "target-list",
        "export_url" : "target-list"
    }
    return render(request, 'targets.html', context=context)

@login_required
def supervisors_view(request):
    """Django view supervisors_views"""
    context = {
        "page_title" : "Supervisors",
        "form" : SupervisorSerializer(),
        "url" : "supervisor-list",
        "export_url" : "supervisorsexport-list"
    }
    return render(request, 'datatables.html', context=context)

@login_required
def shifts_view(request):
    """Django view shifts_view"""
    context = {
        "page_title" : "Shifts",
        "form" : ShiftSerializer(),
        "url" : "shift-list",
        "export_url" : "shiftsexport-list"
    }
    return render(request, 'datatables.html', context=context)
