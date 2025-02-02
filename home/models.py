
from django.contrib.auth.models import User
from login.models import CustomUser
from datetime import datetime, timedelta

from django.db import models
from django.db.models import Count

from login.models import CustomUser

class Personne(models.Model):
    idPers = models.AutoField(primary_key=True)
    nomPers = models.CharField(max_length=42)
    prenomPers = models.CharField(max_length=42)
    mailPers = models.EmailField(max_length=42)
    poidsPers = models.IntegerField()


class Adherent(models.Model):
    idAdh = models.OneToOneField(
        Personne, on_delete=models.CASCADE, primary_key=True, related_name="adherent"
    )
    cotisationPaye = models.BooleanField()


class Poney(models.Model):
    idPon = models.AutoField(primary_key=True)
    nomPon = models.CharField(max_length=42)
    poidsMax = models.IntegerField()


class Cours(models.Model):
    idCours = models.AutoField(primary_key=True)
    idMon = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    idMon = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nbPersMax = models.IntegerField()
    dateCou = models.DateTimeField()
    duree = models.PositiveSmallIntegerField()
    prixCou = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(duree__gte=1) & models.Q(duree__lte=2),
                name="check_duree_range"
            ),
            models.CheckConstraint(
                check=models.Q(nbPersMax__gte=1) & models.Q(nbPersMax__lte=10),
                name="check_nbPersMax_range"
            ),
        ]


class Demande(models.Model):
    demandeur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    idDemande = models.AutoField(primary_key=True)
    dateCou = models.DateTimeField()
    duree = models.PositiveSmallIntegerField()
    accepte = models.BooleanField()
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(duree__gte=1) & models.Q(duree__lte=2),
                name="demande_check_duree_range"
            ),
        ]

class Participer(models.Model):
    idCours = models.ForeignKey(
        Cours, on_delete=models.CASCADE, related_name="participations"
    )
    idPon = models.ForeignKey(
        Poney, on_delete=models.CASCADE, related_name="participations"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["idCours", "idPon"], name="unique_participation")
        ]


class Inscrire(models.Model):
    idCours = models.ForeignKey(
        Cours, on_delete=models.CASCADE, related_name="inscriptions"
    )
    idAdh = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="inscriptions"
    )
    paye = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['idCours', 'idAdh'],
                name='unique_inscription'
            )
        ]

