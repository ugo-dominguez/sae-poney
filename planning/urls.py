from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import ask_private_lesson, planning

urlpatterns = [
    path('planning/', planning, name='planning'),
    path('ask_private_lesson/', ask_private_lesson, name='ask_private_lesson'),
]