# Generated by Django 4.2.4 on 2023-09-02 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0025_custtags_custtags_unq_tag_cust'),
    ]

    operations = [
        migrations.AddField(
            model_name='custmst',
            name='Tags',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]