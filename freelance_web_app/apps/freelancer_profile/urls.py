from django.urls import path

from .views import change_freelancer_profile

urlpatterns = [
    path('', change_freelancer_profile, name='freelancer_profile'),
]
