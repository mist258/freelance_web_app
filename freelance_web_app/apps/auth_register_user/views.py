from django.contrib import messages

from django.shortcuts import render, redirect

from .forms import RegisterUserForm


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

            if password1 == password2:
                user.set_password(password1, password2)
                user.save()

            if choose_role == 'freelancer':
                return redirect('freelancer')

            if choose_role == 'client':
                return redirect('client')

            messages.success(request, f'Your account has been created {username}!')

        else:
            form.add_error('password2', 'Passwords must match')

    else:
        form = RegisterUserForm()

    return render(request, 'register/register_tmpl.html', {'form': form})


def login(request):
    return render(request, 'log_in/log_in.html')

