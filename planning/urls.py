from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import planning, reserver_cours, annuler_reservation, ask_private_lesson


urlpatterns = [
    path('default_planning/', planning, name='default_planning'),
    path('planning/<int:year>/<int:week_number>/', planning, name='planning'),
    path('reserver/<int:id_cours>/', reserver_cours, name='reserver_cours'),
    path('annuler/<int:id_cours>/', annuler_reservation, name='annuler_reserv'),
    path('ask_private_lesson/', ask_private_lesson, name='ask_private_lesson'),
]
