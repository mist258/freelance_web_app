from django.db import models


class UserAbstractModel(models.Model):

    CHOICES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'auth_user'
