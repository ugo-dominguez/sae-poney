from datetime import datetime, timedelta

from django.db import models
from django.db.models import Count
from django.shortcuts import get_object_or_404

from home.models import Cours, Inscrire
from login.models import CustomUser


DAYS = {
    0: "Lundi",
    1: "Mardi",
    2: "Mercredi",
    3: "Jeudi",
    4: "Vendredi",
    5: "Samedi",
    6: "Dimanche",
}

def get_reserved_courses(request, year, week_number):
    reserved_courses = []
    iduser = request.user.id
    if iduser is None: return reserved_courses
    user = get_object_or_404(CustomUser, pk=iduser)

    start_of_week, end_of_week = get_week(year, week_number)
    courses = Cours.objects.annotate(nb_inscriptions=Count('inscriptions')).filter(
        dateCou__range=(start_of_week, end_of_week)
    )

    for course in courses:
        if Inscrire.objects.filter(idCours=course, idAdh=user).exists():
            reserved_courses.append(course)

    return reserved_courses


def get_week(year, week_number):
    first_day_of_year = datetime(year, 1, 1)
    days_to_add = (week_number - 1) * 7 - first_day_of_year.weekday()

    start_of_week = first_day_of_year + timedelta(days=days_to_add)
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

    return start_of_week, end_of_week


def get_courses_by_week(year, week_number):
    start_of_week, end_of_week = get_week(year, week_number)

    courses = Cours.objects.annotate(nb_inscriptions=Count('inscriptions')).filter(
        dateCou__range=(start_of_week, end_of_week)
    )

    courses_by_day = {day: [] for day in DAYS.values()}

    for course in courses:
        day_of_week = course.dateCou.weekday()
        courses_by_day[DAYS[day_of_week]].append(course)

    return courses_by_day
