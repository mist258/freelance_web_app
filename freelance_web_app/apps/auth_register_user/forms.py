from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_countries.fields import CountryField

from freelance_web_app.choises.freelancer_lvl_choices import FreelancerLvlChoices


class FreelancerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password2', 'password1']

    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
    email = forms.EmailField(label='Email Address', required=True)
    skills = forms.CharField(label='Skills', max_length=50)
    experience = forms.CharField(label='Experience', max_length=50)
    level = forms.ChoiceField(choices=FreelancerLvlChoices.choices, widget=forms.RadioSelect)
    location = CountryField(label='Location', blank=True, required=True)
    portfolio_url = forms.URLField(label='Portfolio URL')
    photo_profile = forms.ImageField(label='Profile Picture')


class ClientRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
    email = forms.EmailField(label='Email Address', required=True)
    company_name = forms.CharField(label='Company Name', max_length=50, required=True)
    bio = forms.CharField(label='Bio', widget=forms.Textarea, max_length=500)
    location = CountryField(label='Location', required=True)
    website = forms.URLField(label='Website')
    photo_profile = forms.ImageField(label='Profile Picture')


