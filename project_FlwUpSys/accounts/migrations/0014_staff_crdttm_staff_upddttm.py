# Generated by Django 4.2.4 on 2023-08-19 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_staff_forcereset_staff_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='CrDtTm',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 12, 38, 20, 372786)),
        ),
        migrations.AddField(
            model_name='staff',
            name='UpdDtTm',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 12, 38, 20, 372786)),
        ),
    ]
