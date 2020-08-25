from django.shortcuts import render

# Create your views here.
def dashboard(request):
    """Django view dashboard"""
    return render(request, 'el_dashboard.html')
