from django.db import models

from django_countries.fields import CountryField


class BaseModel(models.Model):
    class Meta:
        abstract = True

    location = CountryField(blank_label='Select your country')
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
