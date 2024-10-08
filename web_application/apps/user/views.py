from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

def register_login_user(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():

            # Create new user but avoid saving yet
            user = form.save(commit=False)
            # set(hashing) password
            user.set_password(form.cleaned_data['password'])

            user.save()
            login(request, user)
            return render(request, 'register/register_tmpl.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register/register_tmpl.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.Post)

        if form.is_valid():
             cd = form.cleaned_data
             user = authenticate(email=cd['email'], password=cd['password'])

             if user is not None:

                 if user.is_active and user.is_client:
                     login(request, user)
                     return redirect(request,  'client_hp/client_home_page.html')

                 if user.is_active and user.is_freelancer:
                     login(request, user)
                     return redirect(request, 'freelancer_hp/freelancer_home_page.html')
                 else:
                     return HttpResponse('Your choise is incorrector account is disabled')

             else:
                return HttpResponse(_('Account does not exist.'))
        else:
            return HttpResponse(_('Password or email is incorrect.'))

    else:
        form = AuthenticationForm()
        return render(request, 'login/login_tmpl.html', {'form': form})
