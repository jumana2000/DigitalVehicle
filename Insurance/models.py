from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Insurance_DB(models.Model):
    period_from = models.DateField()
    period_to = models.DateField()
    engine_no = models.CharField(max_length=13,default=0)
    chassis_no = models.CharField(max_length=17,default=0)
    registration_no = models.CharField(max_length=10,default=0)
    owner_name = models.CharField(max_length=100,default=0)

class I_Register(models.Model):
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)