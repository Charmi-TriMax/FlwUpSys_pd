# Generated by Django 4.2.4 on 2023-08-19 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='city',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='random_password',
        ),
    ]
