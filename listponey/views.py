from django.shortcuts import render
from home.models import Poney

def listponey(request):
    query = request.GET.get('q', '')
    if query:
        poneys = Poney.objects.filter(nomPon__icontains=query)
    else:
        poneys = Poney.objects.all()

    poneys_par_lignes = [poneys[i:i + 5] for i in range(0, len(poneys), 5)]

    return render(request, 'listponey.html', {
        'poneys_par_lignes': poneys_par_lignes,
        'query': query,
    })
