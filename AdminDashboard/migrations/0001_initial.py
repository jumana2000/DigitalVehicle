# Generated by Django 3.0.5 on 2022-07-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='License_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dl_no', models.CharField(max_length=10, null=True)),
                ('holder_name', models.CharField(max_length=20, null=True)),
                ('license_authority', models.CharField(max_length=20, null=True)),
                ('vehicle_class', models.CharField(max_length=20, null=True)),
                ('issue_date', models.DateField(default=0)),
                ('licence_validity', models.DateField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RC_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(default=0, max_length=100)),
                ('registered_rto', models.CharField(default=0, max_length=50)),
                ('maker_model', models.CharField(default=0, max_length=13)),
                ('vehicle_class', models.CharField(default=0, max_length=50)),
                ('fuel_norms', models.CharField(default=0, max_length=30)),
                ('engine_no', models.CharField(default=0, max_length=13)),
                ('chassis_no', models.CharField(default=0, max_length=17)),
                ('registration_date', models.DateField(default=0)),
                ('fitness_upto', models.DateField(default=0)),
                ('insurance_expiry', models.DateField(default=0)),
                ('insurance_expiry_in', models.DateField(default=0)),
                ('registration_no', models.CharField(default=0, max_length=10)),
                ('color', models.CharField(default=0, max_length=20)),
                ('unloaded_weight', models.IntegerField(default=0)),
            ],
        ),
    ]