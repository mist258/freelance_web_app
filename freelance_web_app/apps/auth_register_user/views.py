from django.shortcuts import render


def welcome(request):
    return render(request, 'register/register_tmpl.html')

