# Generated by Django 3.0.5 on 2022-07-05 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDashboard', '0003_license_details_dob'),
        ('Police', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dis_Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(max_length=200)),
                ('amount', models.IntegerField()),
                ('dlid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminDashboard.License_Details')),
            ],
        ),
    ]
