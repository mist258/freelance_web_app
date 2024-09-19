# Generated by Django 5.1 on 2024-09-18 11:16

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos')),
                ('company_name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('website_url', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client Profile',
                'verbose_name_plural': 'Client Profiles',
                'db_table': 'client_profile',
                'ordering': ['id'],
            },
        ),
    ]
