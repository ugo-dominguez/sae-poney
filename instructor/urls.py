from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import manage_planning

urlpatterns = [
    path('', manage_planning, name='manage_planning'),
]