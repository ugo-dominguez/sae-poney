from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsernamePasswordLoginForm(AuthenticationForm):
    INVALID_CREDENTIALS_MESSAGE = _("La combinaison nom d'utilisateur et mot de passe est invalide.")
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': _("Entrez votre nom d'utilisateur"),
            'class': 'form-input username-input'
        }),
        label=''
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': _("Entrez votre mot de passe"),
            'class': 'form-input password-input'
        }),
        label=''
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError(
                self.INVALID_CREDENTIALS_MESSAGE,
                code='invalid_login'
            )

        self.cleaned_data['user'] = user
        return self.cleaned_data

    def get_user(self):
        return self.cleaned_data.get('user')
    

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Arthur',
            'class': 'form-input'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Perticoz',
            'class': 'form-input'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'tom@gmail.com',
            'class': 'form-input'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

