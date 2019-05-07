from django.shortcuts import render
from features.models import Features
from bugs.models import Bugs

# Create your views here.
def all_submissions(request):
    bugs = Bugs.objects.all().order_by('-credits')
    features = Features.objects.all().order_by('-credits')
    return render(request, "submissions.html", {"features": features, "bugs": bugs})
    