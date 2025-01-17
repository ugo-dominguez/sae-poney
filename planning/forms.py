from django import forms


class PrivateLessonForm(forms.Form):
    dateCou = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), label="Date du cours")
    duree = forms.ChoiceField(
        choices=[(1, "1 heure"), (2, "2 heures")],
        label="Durée du cours"
    )
