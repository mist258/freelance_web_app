from django.db import models

from freelance_web_app.core.models import BaseModel
from freelance_web_app.apps.auth_register_user.models import UserModel


class ClientProfile(BaseModel):

    company_name = models.CharField(max_length=100, null=False, blank=False)

    bio = models.TextField()
    website_url = models.URLField(null=False, blank=False)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='client_profile')

    class Meta:
        db_table = 'client_profile'
        ordering = ['id']
        verbose_name = 'Client Profile'
        verbose_name_plural = 'Client Profiles'
