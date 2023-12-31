# Generated by Django 4.2.4 on 2023-08-28 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0013_custaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=5)),
                ('Name', models.CharField(max_length=80)),
                ('Other1', models.CharField(blank=True, max_length=60)),
                ('Other2', models.CharField(blank=True, max_length=60)),
                ('CrDtTm', models.DateTimeField(auto_now_add=True)),
                ('CrBy', models.CharField(blank=True, max_length=60)),
                ('CrFrom', models.CharField(blank=True, max_length=60)),
                ('UpdDtTm', models.DateTimeField(auto_now=True)),
                ('UpdBy', models.CharField(blank=True, max_length=60)),
                ('UpdFrom', models.CharField(blank=True, max_length=60)),
            ],
            options={
                'verbose_name': 'TagMst',
                'db_table': 'TagMst',
            },
        ),
        migrations.CreateModel(
            name='CustTag',
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
                ('TagCode', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Dashboard.tagmst')),
            ],
            options={
                'verbose_name': 'CustTag',
                'db_table': 'CustTag',
            },
        ),
    ]
