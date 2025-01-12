from django.urls import path
from . import views

urlpatterns = [
    path('listponey/', views.listponey, name='listponey'),
]