# Generated by Django 4.2.2 on 2023-08-20 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_staff_crdttm_alter_staff_upddttm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='CrDtTm',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 0, 5, 3, 355400)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='UpdDtTm',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 0, 5, 3, 355400)),
        ),
    ]
