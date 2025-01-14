from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import planning


urlpatterns = [
    path('planning/', planning, name='planning'),
    path('planning/<int:year>/<int:week_number>/', planning, name='planning')
]
