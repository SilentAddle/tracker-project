from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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
            
            #form.user = request.user
            #bug = form.save()
            return redirect(thread, bug.pk)
            #return render(request, "bug_temp.html", {'form': form})
    else:
        form = BugForm()
    return render(request, "bug_form.html", {'form': form})