from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import accept_private_lesson, add_cours, add_poney, dashboard

urlpatterns = [
    path('new_lesson/', add_cours, name='new_lesson'),
    path('new_poney/', add_poney, name='new_poney'),
    path('dashboard/', dashboard, name="dashboard"),
    path('accept_private_lesson/<int:id>', accept_private_lesson, name="accept_private_lesson"),
]