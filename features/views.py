from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Features
from .forms import FeatureForm

# Create your views here.
def all_features(request):
    features = Features.objects.all().order_by('-credits')
    return render(request, "features.html", {"features": features})
    
def thread(request, feature_id):
    feature = get_object_or_404(Features, pk=feature_id)
    return render(request, "feature_thread.html", {"feature": feature})
    
@login_required()
def submit_feature(request, pk=None):
    
    feature = get_object_or_404(Features, pk=pk) if pk else None
    if request.method == "POST":
        user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        #Must add check for credits.
        form = FeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            
            
            feature= form.save(commit=False)
            feature.user= request.user
            feature.save()
    
            user.profile.credits -= 100
            user.profile.save()
            
            return redirect(thread, feature.pk)
    else:
        form = FeatureForm()
    return render(request, "feature_form.html", {'form': form})
    
@login_required()
def updoot_feature(request):
    feature_id = request.POST.get("feature_id")
    credit = request.POST.get("credit")
    
    
    obj = get_object_or_404(Features, pk=feature_id)
    obj.credits += int(credit)
    obj.save()
    
    user_id = request.user.id
    user = get_object_or_404(User, pk=user_id)
    user.profile.credits -= int(credit)
    user.profile.save()
    
    return redirect(thread, feature_id)