from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


CustomUserModel = get_user_model()


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = CustomUserModel
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'role')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        # set up widgets
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'Username',
                                                     'id': 'username',
                                                     })
        self.fields['first_name'].widget.attrs.update({'class': 'form-control',
                                                       'placeholder': 'First Name',
                                                       'id': 'first_name',
                                                       })
        self.fields['last_name'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Last name',
                                                      'id': 'lastname',
                                                    })
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Email',
                                                  'id': 'email',
                                                  'required': 'True',
                                                  'autocomplete': 'email',
                                                  })
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      'type': 'password',
                                                      'required': 'True',
                                                      'id': 'password',
                                                      })
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      'type': 'password',
                                                      'required': 'True',
                                                      'id': 'password',
                                                      })
        self.fields['role'].widget.attrs.update({'class': 'form-control',
                                                        'required': 'True',
                                                        'id': 'role',
                                                        })

    # method will be called when method 'is_valid' is calling
    def cleaned_password(self):
        cd = self.cleaned_data

        if cd['password1'] != cd['password2']:
            raise forms.ValidationError(_('Passwords do not match'))
        return cd['password2']



class LoginUserForm(AuthenticationForm):

    class Meta:
        model = CustomUserModel
        fields = ('email',
                 'password')
    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)

        # set up widgets
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Email',
                                                  'id': 'email',
                                                  'required': 'True',
                                                  'autocomplete': 'email',
                                                  })

        self.fields['password'].widget.attrs.update({'class': 'form-control',
                                                     'type': 'password',
                                                     'required': 'True',
                                                     'id': 'password',
                                                     })
