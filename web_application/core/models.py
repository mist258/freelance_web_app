from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    profile_photo = ... # todo
    location = CountryField(_("Choose your location"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# add url and views todo