# Generated by Django 4.2.4 on 2023-08-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_staff_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='user_type',
            field=models.CharField(choices=[('superuser', 'Superuser'), ('manager', 'Manager'), ('general', 'General')], max_length=20),
        ),
    ]
