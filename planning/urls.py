from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import planning


urlpatterns = [
    path('planning/', planning, name='planning'),
]