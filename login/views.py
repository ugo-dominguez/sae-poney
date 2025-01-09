from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, "Vous êtes connecté avec succès !")
        return super().form_valid(form)
