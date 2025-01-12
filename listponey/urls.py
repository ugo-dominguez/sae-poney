# login/urls.py
from django.urls import path
from .views import listponey

urlpatterns = [
    path('listponey/', listponey, name='listponey'),
]
