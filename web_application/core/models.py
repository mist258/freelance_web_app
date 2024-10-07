from django.db import models

class BaseModel(models.Model):
    profile_photo = ... # todo
    location = ... # todo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# add url and views todo