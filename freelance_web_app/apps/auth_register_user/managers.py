from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, email=None, password=None, **extra_fields):

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        normalize_email = self.normalize_email(email)  # normalize email
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=normalize_email, **extra_fields)
        user.set_password(password)  # hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields['is_staff'] is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields['is_superuser'] is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if extra_fields['is_active'] is not True:
            raise ValueError('Superuser must have is_active=True.')

        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.set_password(password)
        user.save()
        return user
