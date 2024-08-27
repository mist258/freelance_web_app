from django.shortcuts import render


def change_client_profile(request):
    return render(request, 'client_profile_tmpl/client_profile.html')
