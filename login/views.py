
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import get_user_model, login
from .forms import RegistrationForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True 
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if not user.adherent: 
            return redirect("adhesion")
        return redirect("home")  

def register(request):  
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect("adhesion") 
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


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
