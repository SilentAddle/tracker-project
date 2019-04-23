from django.shortcuts import render

# Create your views here.
def all_submissions(request):
    return render(request, "submissions.html")
    