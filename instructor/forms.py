from django import forms

from login.models import CustomUser


class CoursForm(forms.Form):
    idMon = forms.ModelChoiceField(queryset=CustomUser.objects.filter(is_instructor=True).all(), label="Moniteur")
    nbPersMax = forms.IntegerField(min_value=1, max_value=10, label="Nombre de personnes maximum")
    dateCou = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), label="Date du cours")
    duree = forms.ChoiceField(
        choices=[(1, "1 heure"), (2, "2 heures")],
        label="Durée du cours"
    )
    prixCou = forms.DecimalField(max_digits=5, decimal_places=2, label="Prix du cours")

class PoneyForm(forms.Form):
    nomPon = forms.CharField(
        max_length=42, 
        label="Nom du Poney", 
        widget=forms.TextInput(attrs={"placeholder": "Entrez le nom du poney"})
    )
    poidsMax = forms.IntegerField(
        min_value=1, 
        label="Poids maximum (kg)", 
        widget=forms.NumberInput(attrs={"placeholder": "Entrez le poids maximum"})
    )
