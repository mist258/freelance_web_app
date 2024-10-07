from django import forms
from django.contrib.auth.forms import UserChangeForm

from apps.user.models import CustomUserModel
from django_countries.fields import CountryField


class EditFreelancerProfile(UserChangeForm):

    LVL_CHOICES = [
        ('trainee', 'Trainee'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
    ]

    class Meta:
        model = CustomUserModel
        fields = ('username', 'first_name', 'last_name')

    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email',
               'class': 'form-control',
               'id': 'email',
               'required': 'True',
               }
    ))
    level = forms.ChoiceField(label='Choose level:', required=True, choices=LVL_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control',
               'id': 'level',
               }
    ))
    skills = forms.CharField(label='Skills:', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Enter your skills separated by comma',
               'rows': 4,
               'cols': 40,
               'id': 'skills',
               }
    ))
    experience = forms.CharField(label='Experience:', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Describe key highlights of your development experience',
               'rows': 6,
               'cols': 40,
               'id': 'experience',
               }
    ))
    portfolio_url = forms.URLField(label='Enter yours portfolio url:', widget=forms.URLInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter your portfolio url',
               'id': 'portfolio_url',
               }
    ))
    profile_photo = forms.ImageField(widget=forms.ClearableFileInput)

    location = CountryField().formfield(label='Choose your country', required=True, widget=forms.Select(
        attrs={'class': 'form-control',
               'id': 'location',
               }
    ))