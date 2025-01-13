from django import forms
from login.models import CustomUser
from home.models import Cours


class CoursForm(forms.Form):
    idMon = forms.ModelChoiceField(queryset=CustomUser.objects.filter(is_superuser=True).all(), label="Moniteur")
    nbPersMax = forms.IntegerField(min_value=1, max_value=10, label="Nombre de personnes maximum")
    dateCou = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), label="Date du cours")
    duree = forms.ChoiceField(
        choices=[(1, "1 heure"), (2, "2 heures")],
        label="Durée du cours"
    )
    prixCou = forms.DecimalField(max_digits=5, decimal_places=2, label="Prix du cours")
