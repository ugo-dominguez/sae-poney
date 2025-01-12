from django.shortcuts import render


def planning(request):
    context = {}
    return render(request, 'planning.html', context)
