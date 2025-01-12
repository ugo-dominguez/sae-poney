from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import render

from .forms import CoursForm
from .models import ajouter_cours


@user_passes_test(lambda u: u.is_superuser)
def manage_planning(request):
    if request.method == "POST":
        form = CoursForm(request.POST)
        if form.is_valid():
            return ajouter_cours(request) 
        return JsonResponse({"error": "Données invalides", "details": form.errors}, status=400)
    else:
        form = CoursForm()
    
    return render(request, "manage.html", {"form": form})
