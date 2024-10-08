from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractUser


class CustomUserModel(AbstractUser, PermissionsMixin):

    CHOICES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    ]

    first_name = models.CharField(_("First Name"), max_length=40)
    last_name = models.CharField(_("Last Name"), max_length=40)
    username = models.CharField(_("Username"), max_length=40, unique=True,
                                error_messages={
        "unique": _("A user with that username already exists."),
    }
                                )
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(_("Role"), max_length=10, choices=CHOICES)
    is_active = models.BooleanField(_("Is active"), default=True)
    is_staff = models.BooleanField(_("Is staff"), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'CustomUserModel'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}'

    def is_freelancer(self):
        return self.role == 'freelancer'

    def is_client(self):
        return self.role == 'client'

    objects = CustomUserManager()
