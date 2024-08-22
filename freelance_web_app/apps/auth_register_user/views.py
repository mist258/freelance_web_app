from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegisterUserForm, LoginUserForm


def register(request):

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():

            user = form.save()
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            choose_role = form.cleaned_data['choose_role']

            if password1 != password2:
                form.add_error('password1', 'Passwords must match')

            else:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.set_password(password1)
                user.save()

            if choose_role == 'freelancer':
                return redirect('success')

            if choose_role == 'client':
                return redirect('success')

            messages.success(request, f'Your account has been created {username}!')
            return redirect('success')

        else:
            form.add_error('password2', 'Passwords must match')

    else:
        form = RegisterUserForm()

    return render(request, 'register/register_tmpl.html', {'form': form})


def login_page(request):

    if request.method == 'POST':
        form = LoginUserForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('success')

    else:
        form = LoginUserForm()

    return render(request, 'log_in/log_in.html', {'form': form})


def success_page(request):
    return render(request, 'register_success/success_tmpl.html')








