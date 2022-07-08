# Generated by Django 3.0.5 on 2022-07-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0003_dl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reported', models.DateField()),
                ('body_style', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('marker_plate_no', models.CharField(max_length=10)),
                ('vehicle_registered', models.BooleanField()),
                ('vehicle_register_state', models.CharField(max_length=10)),
                ('vehicle_identification_no', models.IntegerField()),
                ('door_locked', models.BooleanField()),
                ('keys_in_vehicle', models.BooleanField()),
                ('name_of_insurance_company', models.CharField(max_length=10)),
                ('owner_name', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=10)),
                ('court_available', models.BooleanField()),
                ('date_of_stolen', models.DateField()),
                ('day_of_week', models.CharField(max_length=10)),
                ('time', models.TimeField()),
                ('location_from', models.CharField(max_length=10)),
            ],
        ),
    ]
