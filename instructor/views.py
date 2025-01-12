from django.contrib import messages  # Import pour les messages
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import CoursForm
from .models import ajouter_cours


@user_passes_test(lambda u: u.is_superuser)
def add_cours(request):
    if request.method == "POST":
        form = CoursForm(request.POST)
        if form.is_valid():
            ajouter_cours(request)
            messages.success(request, "Le cours a été ajouté avec succès !")
            return redirect("new_lesson")
        else:
            messages.error(request, "Erreur lors de l'ajout du cours. Vérifiez les données fournies.")
            return redirect("new_lesson")
    else:
        form = CoursForm()
    
    return render(request, "manage.html", {"form": form})
