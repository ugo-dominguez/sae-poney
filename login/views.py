from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def adhesion(request):
    if request.method == "POST":
        if 'oui' in request.POST:  
            request.user.adherent = True
            request.user.save()
            return redirect("home")  
        elif 'non' in request.POST:  
            return redirect("home")  
    return render(request, "adhesion.html")
