# Generated by Django 5.1 on 2024-08-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_register_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
