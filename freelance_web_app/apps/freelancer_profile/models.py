from django.db import models

from freelance_web_app.core.models import BaseModel
from freelance_web_app.apps.auth_register_user.models import UserModel


class FreelancerProfile(BaseModel):
    LVL_CHOICES = [
        ('trainee', 'Trainee'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    level = models.CharField(max_length=20, choices=LVL_CHOICES,)
    skills = models.CharField(max_length=200, null=True, blank=True)
    experience = models.CharField(max_length=200, null=True, blank=True)
    portfolio_url = models.URLField(null=True, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='freelancer_profile')

    class Meta:

        db_table = 'freelancer_profile'
        ordering = ['id']
        verbose_name = 'Freelancer Profile'
        verbose_name_plural = 'Freelancer Profiles'
