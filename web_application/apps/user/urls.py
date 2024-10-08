from django.urls import path
from .views import register_login_user, login_user
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register', register_login_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

]