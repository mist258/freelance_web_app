from core.models import BaseModel
from django.db import models
from apps.user.models import  CustomUserModel

class FreelancerProfile(BaseModel):

    LVL_CHOICES = [
        ('trainee', 'Trainee'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    level = models.CharField(max_length=20, choices=LVL_CHOICES)
    skills = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    portfolio_url = models.URLField(max_length=80, null=True, blank=True)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='freelancer_profile')

    class Meta:
        db_table = 'freelancer_profile'
        verbose_name = 'Freelancer Profile'
        verbose_name_plural = 'Freelancer Profiles'
        ordering = ['id']
