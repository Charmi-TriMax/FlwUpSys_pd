# Generated by Django 4.2.4 on 2023-08-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_staff_city_remove_staff_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='city',
            field=models.CharField(default='baroda', max_length=100),
            preserve_default=False,
        ),
    ]
