from django.shortcuts import render

def listponey(request):
    context = {}
    return render(request, 'listponey.html', context)
