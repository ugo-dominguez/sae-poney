from django.contrib import messages  # Import pour les messages
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import redirect, render

from home.models import Cours

from .forms import CoursForm, PoneyForm
from .models import ajouter_cours, ajouter_poney


@user_passes_test(lambda u: u.is_instructor)
def add_cours(request):
    if request.method == "POST":
        form = CoursForm(request.POST)
        if form.is_valid():
            ajouter_cours(request)
            messages.success(request, "Le cours a été ajouté avec succès !")
            return redirect("dashboard")
        else:
            messages.error(request, "Erreur lors de l'ajout du cours. Vérifiez les données fournies.")
            return redirect("dashboard")
    
    else:
        return redirect("dashboard")

@user_passes_test(lambda u: u.is_instructor)
def add_poney(request):
    if request.method == "POST":
        form = PoneyForm(request.POST)
        if form.is_valid():
            ajouter_poney(request)
            messages.success(request, "Le poney a été ajouté avec succès !")
            return redirect("dashboard")
        
        else:
            messages.error(request, "Erreur lors de l'ajout du poney. Vérifiez les données fournies.")
            return redirect("dashboard")
    
    else:
        return redirect("dashboard")

@user_passes_test(lambda u: u.is_instructor)
def dashboard(request):
    lessons = Cours.objects.filter(idMon=request.user)
    days = {}
    for lesson in lessons:
        date = str(lesson.dateCou)[:-15]
        lesson.time = str(lesson.dateCou)[-15:-9]
        days[date] = days.get(date, []) + [lesson]
    
    return render(request, "dashboard.html", {
        "days": days,
        "new_lesson_form": CoursForm(),
        "new_poney_form": PoneyForm(),
    })
