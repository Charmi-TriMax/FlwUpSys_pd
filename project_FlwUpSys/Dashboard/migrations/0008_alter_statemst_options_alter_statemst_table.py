# Generated by Django 4.2.4 on 2023-08-23 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_alter_citymst_options_citymst_unq_statecode_cityname_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statemst',
            options={'verbose_name': 'StateMst'},
        ),
        migrations.AlterModelTable(
            name='statemst',
            table='StateMst',
        ),
    ]
