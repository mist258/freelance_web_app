
from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return render(request, 'register/register_tmpl.html')


def login(request):
    pass


def logout(request):
    pass


