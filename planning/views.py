from datetime import datetime

from django.shortcuts import render

from .models import get_week, get_courses_by_week


def planning(request, 
        year=datetime.now().year,
        week_number=datetime.now().isocalendar().week):
    
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

    start, end = get_week(year, week_number)
    courses_by_week = get_courses_by_week(year, week_number)

    return render(request, 'planning.html', {
        "year": year,
        "week": week_number,
        "week_planning": courses_by_week,
        "start": start.date(),
        "end": end.date(),
    })
