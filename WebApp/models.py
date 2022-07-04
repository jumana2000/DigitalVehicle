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