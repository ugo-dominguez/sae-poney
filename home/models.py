from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


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
    idMon = models.ForeignKey(User, on_delete=models.CASCADE)
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
        Adherent, on_delete=models.CASCADE, related_name="inscriptions"
    )
    paye = models.BooleanField()


DAYS = {
    0: "Lundi",
    1: "Mardi",
    2: "Mercredi",
    3: "Jeudi",
    4: "Vendredi",
    5: "Samedi",
    6: "Dimanche",
}

def get_courses_by_week(year, week_number):
    first_day_of_year = datetime(year, 1, 1)
    days_to_add = (week_number - 1) * 7 - first_day_of_year.weekday()

    start_of_week = first_day_of_year + timedelta(days=days_to_add)
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

    courses = Cours.objects.annotate(nb_inscriptions=Count('inscriptions')).filter(
        dateCou__range=(start_of_week, end_of_week)
    )

    courses_by_day = {day: [] for day in DAYS.values()}

    for course in courses:
        day_of_week = course.dateCou.weekday()
        courses_by_day[DAYS[day_of_week]].append(course)

    return courses_by_day
