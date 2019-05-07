from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Bugs
from .forms import BugForm

# Create your views here.
def all_bugs(request):
    bugs = Bugs.objects.all().order_by('-credits')
    return render(request, "bugs.html", {"bugs": bugs})
    
def thread(request, bug_id):
    bug = get_object_or_404(Bugs, pk=bug_id)
    return render(request, "bug_thread.html", {"bug": bug})
    
@login_required()
def submit_bug(request, pk=None):
    
    bug = get_object_or_404(Bugs, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            
            
            bug= form.save(commit=False)
            bug.user= request.user
            bug.save()
            
            return redirect(thread, bug.pk)
    else:
        form = BugForm()
    return render(request, "bug_form.html", {'form': form})
    
@login_required()
def updoot_bug(request):
    bug_id = request.POST.get("bug_id")
    credit = request.POST.get("credit")
    
    
    obj = get_object_or_404(Bugs, pk=bug_id)
    obj.credits += int(credit)
    obj.save()
    
    user_id = request.user.id
    user = get_object_or_404(User, pk=user_id)
    user.profile.credits -= int(credit)
    user.profile.save()
    
    return redirect(thread, bug_id)