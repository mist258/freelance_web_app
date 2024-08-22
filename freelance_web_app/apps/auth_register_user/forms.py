from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):

    CHOICES = [
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    ]
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'First name', 'id': 'firstname'}),
                                max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Last name', 'id': 'lastname'}),
                                max_length=50, required=True)
    username = forms.CharField(label='Username', widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username'}),
                                max_length=50, required=True)
    email = forms.EmailField(label='Email', widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email',
                                       'required': 'True', 'autocomplete': 'email'}),
                                required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 'input_type': 'password', 'required': 'True', 'id':'password'}),
                                required=True, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 'input_type': 'password', 'required': 'True', 'id':'password'}),
                                required=True)
    choose_role = forms.ChoiceField(label='Role', choices=CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'choose_role')


class LoginUserForm(forms.ModelForm):

    email = forms.EmailField(label='Email', widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email',
                                       'required': 'True', 'autocomplete': 'email'}),
                                required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 'input_type': 'password', 'required': 'True',
                                       'id': 'password'}),
                                required=True)

    class Meta:
        model = UserModel
        fields = ('email', 'password')

