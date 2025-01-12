from django.contrib.auth.models import User
from django.db import models
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from home.models import Cours


def ajouter_cours(request):
    if request.method == "POST":
        idMon = request.POST.get("idMon")
        nbPersMax = request.POST.get("nbPersMax")
        dateCou = request.POST.get("dateCou")
        duree = request.POST.get("duree")
        prixCou = request.POST.get("prixCou")
        
        moniteur = get_object_or_404(User, pk=idMon)
        
        cours = Cours.objects.create(
            idMon=moniteur,
            nbPersMax=nbPersMax,
            dateCou=dateCou,
            duree=duree,
            prixCou=prixCou
        )
        
        return JsonResponse({"message": "Cours ajouté avec succès", "idCours": cours.idCours})
    
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)
