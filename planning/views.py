from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

from home.models import Demande, get_courses_by_week

from .forms import PrivateLessonForm


def ask_private_lesson(request):
    if request.method == "POST":
        dateCou = request.POST.get("dateCou")
        duree = request.POST.get("duree")
        user = request.user
        
        try:
            Demande.objects.create(
                demandeur=user,
                dateCou=dateCou,
                duree=duree,
                accepte=False,
            )        
        except Exception:
            return JsonResponse({"message": "Erreur lors de la création de la demande"})
        
        return JsonResponse({"message": "Demande prise en compte avec succès"})


def planning(request):
    year = datetime.now().year
    week_number = datetime.now().isocalendar().week
    courses_by_week = get_courses_by_week(year, week_number)

    # à delete
    for cours in courses_by_week["Jeudi"]:
        cours.nb_inscriptions += 5

    return render(request, 'planning.html', {
        "week_planning": courses_by_week,
        "week_number": week_number,
        "private_lesson_form": PrivateLessonForm(),
    })
