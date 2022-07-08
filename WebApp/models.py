from ctypes import addressof
from django.db import models
from AdminDashboard.models import *
from Core.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class RC_Dashboard(models.Model):
    rid = models.ForeignKey(RC_Details,on_delete=CASCADE,null=True,blank=False)
    userid = models.ForeignKey(User,on_delete=CASCADE,null=True,blank=False)
    engine_no = models.CharField(max_length=20,null=True,blank=False)
    chassis_no = models.CharField(max_length=20,null=True,blank=False)

class DL(models.Model):
    dob = models.DateField()
    dlid = models.ForeignKey(License_Details,on_delete=CASCADE)
    userid = models.ForeignKey(User,on_delete=CASCADE,null=True,blank=False)

class Complaint(models.Model):
    date_reported = models.DateField()
    body_style = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    marker_plate_no = models.CharField(max_length=10)
    vehicle_registered = models.BooleanField()
    vehicle_register_state = models.CharField(max_length=10)
    vehicle_identification_no = models.IntegerField()
    door_locked = models.BooleanField()
    keys_in_vehicle = models.BooleanField()
    name_of_insurance_company = models.CharField(max_length=10)
    owner_name = models.CharField(max_length=10)
    phone = models.IntegerField()
    address = models.CharField(max_length=10)
    court_available = models.BooleanField()
    date_of_stolen = models.DateField()
    day_of_week = models.CharField(max_length=10)
    time = models.TimeField()
    location_from = models.CharField(max_length=10)

