from django.db import models


from freelance_web_app.apps.user.models import UserAbstractModel


class ClientProfileModel(UserAbstractModel):
    class Meta:
        db_table = 'client_profile'

    company_name = models.CharField(max_length=60)
    bio = models.TextField(max_length=500, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    rating = models.FloatField(default=0)
