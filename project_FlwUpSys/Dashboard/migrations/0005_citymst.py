# Generated by Django 4.2.4 on 2023-08-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Other1', models.CharField(blank=True, max_length=60)),
                ('Other2', models.CharField(blank=True, max_length=60)),
                ('CrDtTm', models.DateTimeField(auto_now_add=True)),
                ('CrBy', models.CharField(blank=True, max_length=60)),
                ('CrFrom', models.CharField(blank=True, max_length=60)),
                ('UpdDtTm', models.DateTimeField(auto_now=True)),
                ('UpdBy', models.CharField(blank=True, max_length=60)),
                ('UpdFrom', models.CharField(blank=True, max_length=60)),
            ],
        ),
    ]
