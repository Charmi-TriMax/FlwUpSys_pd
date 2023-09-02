# Generated by Django 4.2.4 on 2023-08-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0006_citymst_name_citymst_state_citymst_statecode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citymst',
            options={'verbose_name': 'CityMst'},
        ),
        migrations.AddConstraint(
            model_name='citymst',
            constraint=models.UniqueConstraint(fields=('StateCode', 'Name'), name='unq_StateCode_CityName'),
        ),
        migrations.AlterModelTable(
            name='citymst',
            table='CityMst',
        ),
    ]