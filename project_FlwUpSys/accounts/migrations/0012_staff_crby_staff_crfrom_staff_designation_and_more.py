# Generated by Django 4.2.4 on 2023-08-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_staff_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='CrBy',
            field=models.CharField(default='abc', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='CrFrom',
            field=models.CharField(default='xyz', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Designation',
            field=models.CharField(default='stu', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Other1',
            field=models.CharField(default='a', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Other2',
            field=models.CharField(default='b', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Phone',
            field=models.CharField(default='123456789', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='UpdBy',
            field=models.CharField(default='bcd', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='UpdFrom',
            field=models.CharField(default='jkl', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='mobile',
            field=models.CharField(default=7845123698, max_length=50),
            preserve_default=False,
        ),
    ]
