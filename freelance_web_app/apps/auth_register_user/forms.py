from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):

    CHOICES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    ]

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(), max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(), max_length=50, required=True)
    username = forms.CharField(label='Username', max_length=50, required=True)
    email = forms.EmailField(label='Email', widget=forms.TextInput(), required=True, unique=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), required=True)
    choose_role = forms.ChoiceField(label='Role', choices=CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', 'choose_role')


class LoginUserForm(forms.ModelForm):

    email = forms.EmailField(label='Email', widget=forms.TextInput(), required=True, unique=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ('email', 'password')

