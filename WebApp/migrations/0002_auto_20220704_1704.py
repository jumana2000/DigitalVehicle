# Generated by Django 3.0.5 on 2022-07-04 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AdminDashboard', '0002_auto_20220701_1632'),
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rc_dashboard',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rc_dashboard',
            name='chassis_no',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rc_dashboard',
            name='engine_no',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='rc_dashboard',
            name='rid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminDashboard.RC_Details'),
        ),
    ]
