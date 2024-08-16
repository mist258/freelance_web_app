from django.db import models
from django_countries.fields import CountryField


class UserAbstractModel(models.Model):

    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    location = CountryField(blank_label='Select a location')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_freelancer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
