from django.db import models
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from home.models import Cours, Poney
from login.models import CustomUser

from .forms import PoneyForm


def ajouter_cours(request):
    if request.method == "POST":
        idMon = request.POST.get("idMon")
        nbPersMax = request.POST.get("nbPersMax")
        dateCou = request.POST.get("dateCou")
        duree = request.POST.get("duree")
        prixCou = request.POST.get("prixCou")
        
        moniteur = get_object_or_404(CustomUser, pk=idMon)
        
        cours = Cours.objects.create(
            idMon=moniteur,
            nbPersMax=nbPersMax,
            dateCou=dateCou,
            duree=duree,
            prixCou=prixCou
        )
        
        return JsonResponse({"message": "Cours ajouté avec succès", "idCours": cours.idCours})
    
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

def ajouter_poney(request):
    if request.method == "POST":
        try:    
            Poney.objects.create(
                nomPon=request.POST.get("nomPon"),
                poidsMax=request.POST.get("poidsMax")
            )
        except Exception:
            return JsonResponse({"message": "Erreur"})
        
        return JsonResponse({"message": "Poney ajouté avec succès"})
    
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)