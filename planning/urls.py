from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import planning, reserver_cours


urlpatterns = [
    path('default_planning/', planning, name='default_planning'),
    path('planning/<int:year>/<int:week_number>/', planning, name='planning'),
    path('inscrire/<int:cours_id>/', reserver_cours, name='reserver_cours')
]
