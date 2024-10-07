from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    pass

class LoginUserForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput( attrs={'class': 'form-control',
                                       'placeholder': 'Email',
                                       'id': 'email',
                                       'required': 'True',
                                       'autocomplete': 'email'}),
                                        required=True)

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'input_type': 'Password',
                                                                                   'id': 'password',
                                                                                   'required': 'True',}),
                                                                                    required=True)
