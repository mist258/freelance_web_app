from django.db import models


class FreelancerLvlChoices(models.TextChoices):
    Trainee = 'Trainee'
    Junior = 'Junior'
    Middle = 'Middle'
    Senior = 'Senior'
