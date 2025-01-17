from datetime import datetime

from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render

from home.models import Cours, Demande, Inscrire
from login.models import CustomUser

from .forms import PrivateLessonForm
from .models import get_courses_by_week, get_reserved_courses, get_week


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
            messages.error(request, "Erreur lors de la création de la demande")
        else:
            messages.success(request, "Demande prise en compte avec succès")
    
    return render(request, 'private-lessson.html', {"private_lesson_form": PrivateLessonForm()})


def reserver_cours(request, id_cours):
    try:
        iduser = request.user.id

        if iduser is None:
            raise AttributeError("Vous n'êtes pas connecté !")
        
        user = get_object_or_404(CustomUser, pk=iduser)
        course = Cours.objects.get(idCours=id_cours)
        Inscrire.objects.create(idCours=course, idAdh=user, paye=True)
        
    except AttributeError as e:
        messages.error(request, e)
    except Exception as e:
        messages.error(request, "Une erreur s'est produite lors de l'inscription.")
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/default_planning/'))


def annuler_reservation(request, id_cours):
    iduser = request.user.id
    user = get_object_or_404(CustomUser, pk=iduser)
    course = get_object_or_404(Cours, idCours=id_cours)

    existing_inscription = Inscrire.objects.filter(idCours=course, idAdh=user).first()
    existing_inscription.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/default_planning/'))


def manage_action(request, year, week_number):
    action = request.GET.get('action')
    match action:
        case 'prev':
            week_number -= 1

        case 'next':
            week_number += 1

    if week_number < 1:
        week_number = 52
        year -= 1
    elif week_number > 52:
        week_number = 1
        year += 1

    return year, week_number


def planning(request, 
        year=datetime.now().year,
        week_number=datetime.now().isocalendar().week):

    year, week_number = manage_action(request, year, week_number)

    start, end = get_week(year, week_number)
    courses_by_week = get_courses_by_week(year, week_number)
    reserved = get_reserved_courses(request, year, week_number)

    return render(request, 'planning.html', {
        "year": year,
        "week": week_number,
        "week_planning": courses_by_week,
        "start": start.date(),
        "end": end.date(),
        "reserved": reserved,
        "week_number": week_number,
    })
