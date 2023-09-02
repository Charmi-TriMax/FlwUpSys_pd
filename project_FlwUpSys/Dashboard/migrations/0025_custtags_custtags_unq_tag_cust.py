# Generated by Django 4.2.4 on 2023-08-29 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0024_alter_custmst_othcityareaid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustTags',
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
                ('Cust', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Dashboard.custmst')),
                ('Tag', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Dashboard.tagmst')),
            ],
            options={
                'verbose_name': 'CustTag',
                'db_table': 'CustTag',
            },
        ),
        migrations.AddConstraint(
            model_name='custtags',
            constraint=models.UniqueConstraint(fields=('Tag', 'Cust'), name='unq_Tag_Cust'),
        ),
    ]
