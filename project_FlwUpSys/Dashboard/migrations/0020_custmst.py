# Generated by Django 4.2.4 on 2023-08-28 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0019_remove_groupmst_unq_code_groupname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('GrpMstCode', models.CharField(default='GEN', max_length=5)),
                ('RespPrsnNm', models.CharField(blank=True, max_length=80)),
                ('RespPrsnMbl', models.CharField(blank=True, max_length=50)),
                ('ContPrsnNm', models.CharField(blank=True, max_length=80)),
                ('ContPrsnMbl', models.CharField(blank=True, max_length=50)),
                ('Addr1', models.CharField(max_length=100)),
                ('Addr2', models.CharField(blank=True, max_length=100)),
                ('Addr3', models.CharField(blank=True, max_length=100)),
                ('StateCode', models.IntegerField(default=24)),
                ('Pincode', models.CharField(blank=True, max_length=10)),
                ('Country', models.CharField(default='India', max_length=50)),
                ('Mobile', models.CharField(blank=True, max_length=50)),
                ('Phone', models.CharField(blank=True, max_length=50)),
                ('EMail', models.CharField(blank=True, max_length=120)),
                ('OthContPrsnNm', models.CharField(blank=True, max_length=80)),
                ('OthContPrsnMbl', models.CharField(blank=True, max_length=50)),
                ('OthAddr1', models.CharField(blank=True, max_length=100)),
                ('OthAddr2', models.CharField(blank=True, max_length=100)),
                ('OthAddr3', models.CharField(blank=True, max_length=100)),
                ('OthStateCode', models.IntegerField(blank=True, default=24)),
                ('OthPincode', models.CharField(blank=True, max_length=10)),
                ('OthCountry', models.CharField(blank=True, default='India', max_length=50)),
                ('OthMobile', models.CharField(blank=True, max_length=50)),
                ('OthPhone', models.CharField(blank=True, max_length=50)),
                ('OthEMail', models.CharField(blank=True, max_length=120)),
                ('WebAddr', models.CharField(blank=True, max_length=120)),
                ('SplRemarks', models.CharField(blank=True, max_length=200)),
                ('GSTNo', models.CharField(blank=True, max_length=20)),
                ('PANNo', models.CharField(blank=True, max_length=20)),
                ('Other1', models.CharField(blank=True, max_length=60)),
                ('Other2', models.CharField(blank=True, max_length=60)),
                ('CrDtTm', models.DateTimeField(auto_now_add=True)),
                ('CrBy', models.CharField(blank=True, max_length=60)),
                ('CrFrom', models.CharField(blank=True, max_length=60)),
                ('UpdDtTm', models.DateTimeField(auto_now=True)),
                ('UpdBy', models.CharField(blank=True, max_length=60)),
                ('UpdFrom', models.CharField(blank=True, max_length=60)),
                ('CityAreaID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='custmst_cityarea', to='Dashboard.cityarea')),
                ('CityMstID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='custmst_citymst', to='Dashboard.citymst')),
                ('GrpMstID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Dashboard.groupmst')),
                ('OthCityAreaID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='custmst_othcityarea', to='Dashboard.cityarea')),
                ('OthCityMstID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='custmst_othcitymst', to='Dashboard.citymst')),
                ('OthStateMstID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='custmst_othstatemst', to='Dashboard.statemst')),
                ('StateMstID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='custmst_statemst', to='Dashboard.statemst')),
            ],
        ),
    ]