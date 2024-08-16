from django.db import models


from freelance_web_app.apps.user.models import UserAbstractModel


class AdminProfileModel(UserAbstractModel):
    class Meta:
        db_table = 'admin_profile'

    admin_since = models.DateField(null=True)

