from django.db import models
from apps.user.models import CustomUserModel
from core.models import BaseModel

class ClientProfile(BaseModel):
    company_name = models.CharField(max_length=80, null=False, blank=False)
    bio = models.TextField(null=False, blank=False)
    website_url = models.URLField(max_length=100, null=False, blank=False)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='client_profile')

    class Meta:
        db_table = 'client_profile'
        verbose_name = 'Client Profile'
        verbose_name_plural = 'Client Profiles'
        ordering = ['id'
                    ]

