from django.urls import path
from .views import change_client_profile

urlpatterns = [
    path('', change_client_profile, name='client_profile'),
]
