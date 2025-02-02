from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLoginView, register, adhesion

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),   
    path('adhesion/', adhesion, name='adhesion') 
]
