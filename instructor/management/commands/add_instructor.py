from django.core.management.base import BaseCommand
from home.models import CustomUser

class Command(BaseCommand):
    help = "Ajoute un moniteur à la base de données"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help="Nom d'utilisateur du moniteur")
        parser.add_argument('email', type=str, help="Adresse email du moniteur")
        parser.add_argument('password', type=str, help="Mot de passe du moniteur")

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']

        if CustomUser.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f"L'utilisateur '{username}' existe déjà !"))
            return

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_instructor = True  
        user.save()

        self.stdout.write(self.style.SUCCESS(f"Moniteur '{username}' ajouté avec succès !"))
