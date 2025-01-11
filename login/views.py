from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, "Vous êtes connecté avec succès !")
        return super().form_valid(form)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès ! Veuillez vous connecter.")
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})
