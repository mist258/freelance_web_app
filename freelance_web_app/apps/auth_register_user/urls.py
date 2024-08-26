from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('success/', views.success_page, name='success'),

]
