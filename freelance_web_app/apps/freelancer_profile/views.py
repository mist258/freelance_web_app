from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm






def change_freelancer_profile(request):
    return render(request, 'freelancer_profile_tmpl/freelancer_profile.html')
