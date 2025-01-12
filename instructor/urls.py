from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import add_cours

urlpatterns = [
    path('new_lesson/', add_cours, name='new_lesson'),
]