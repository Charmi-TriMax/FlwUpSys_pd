# Generated by Django 4.2.2 on 2023-08-20 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_staff_crdttm_staff_upddttm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='CrDtTm',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 20, 23, 51, 51, 396603)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='UpdDtTm',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 20, 23, 51, 51, 396603)),
        ),
    ]