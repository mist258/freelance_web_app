from django.db import models

from freelance_web_app.apps.user.models import UserAbstractModel
from freelance_web_app.choises.freelancer_lvl_choices import FreelancerLvlChoices


class FreelancerProfileModel(UserAbstractModel):
    class Meta:
        db_table = 'freelancer_profile'

    level = models.CharField(max_length=7, choices=FreelancerLvlChoices.choices)
    skills = models.TextField()
    experience = models.TextField()
    portfolio_url = models.URLField(blank=True, null=True)
    rating = models.FloatField(default=0)
