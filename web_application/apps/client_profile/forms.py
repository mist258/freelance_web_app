from django import forms
from django.contrib.auth.forms import UserChangeForm

from apps.user.models import CustomUserModel
from django_countries.fields import CountryField


class EditFreelancerProfile(UserChangeForm):

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
    bio = forms.CharField(label='Describe the key aspects of your company\'s works.', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'bio',
        'placeholder': 'About your company',
        'rows': '6',
        'cols': '40',
                }
    ))
    website_url = forms.URLField(label='Enter yours portfolio url:', widget=forms.URLInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter your portfolio url',
               'id': 'website_url',
               }
    ))
    profile_photo = forms.ImageField(widget=forms.ClearableFileInput)
    location = CountryField().formfield(label='Choose your country', required=True, widget=forms.Select(
        attrs={'class': 'form-control',
               'id': 'location',
               }
    ))