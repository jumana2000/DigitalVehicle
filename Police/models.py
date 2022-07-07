from django.db import models
from AdminDashboard.models import *
from django.db.models.deletion import CASCADE
# Create your models here.

class Police(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Dis_Action(models.Model):
    reason = models.TextField(max_length=200)
    amount = models.IntegerField()
    dlid = models.ForeignKey(License_Details,on_delete=CASCADE)
