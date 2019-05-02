from django.shortcuts import render

# Create your views here.
def about(request):
    """Return Index HTML"""
    return render(request, 'index.html')