from django.shortcuts import render


def change_freelancer_profile(request):
    return render(request, 'freelancer_profile_tmpl/frelancer_profile.html')
