from datetime import datetime

from django.shortcuts import render

from home.models import get_courses_by_week


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
    })
