from django.shortcuts import render


def register(request):
    return render(request, 'register/register_tmpl.html')


def login(request):
    return render(request, 'log_in/log_in.html')




