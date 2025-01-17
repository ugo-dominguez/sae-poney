from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    adherent = models.BooleanField(default=False)  
    is_instructor = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
      
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions', 
        blank=True
    )