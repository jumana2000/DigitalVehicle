# Generated by Django 3.0.5 on 2022-07-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Police', '0002_dis_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='dis_action',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dis_action',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
