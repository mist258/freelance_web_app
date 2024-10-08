from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    profile_photo = models.ImageField(upload_to='user/profile_photos/')
    location = CountryField(_("Choose your location"), null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

