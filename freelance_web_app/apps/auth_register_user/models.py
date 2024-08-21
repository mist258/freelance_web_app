from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class UserModel(AbstractBaseUser, PermissionsMixin):

    CHOICES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True, error_messages={
        'unique': "A user with that username already exists.",
    },)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        db_table = 'auth_user'
        ordering = ['id']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def is_client(self):
        return self.role == 'client'

    def is_freelancer(self):
        return self.role == 'freelancer'

    objects = CustomUserManager()

