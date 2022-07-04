from django.db import models

# Create your models here.

class RC_Details(models.Model):
    owner_name = models.CharField(max_length=100,default=0)
    registered_rto = models.CharField(max_length=50,default=0)
    maker_model = models.CharField(max_length=13,default=0)
    vehicle_class = models.CharField(max_length=50,default=0)
    fuel_norms = models.CharField(max_length=30,default=0)
    engine_no = models.CharField(max_length=13,default=0)
    chassis_no = models.CharField(max_length=17,default=0)
    registration_date = models.DateField(default = 0)
    fitness_upto = models.DateField(default = 0)
    insurance_expiry = models.DateField(default = 0)
    insurance_expiry_in = models.DateField(default = 0)
    registration_no = models.CharField(max_length=10,default=0)
    color = models.CharField(max_length=20,default=0)
    unloaded_weight = models.IntegerField(default=0)
    
    def __str__(self):
        return self.registration_no


class License_Details(models.Model):
    dl_no = models.CharField(max_length=10,null=True,default=False)
    holder_name = models.CharField(max_length=20,null=True,default=False)
    authority_code = models.CharField(max_length=5,default=False)
    license_authority = models.CharField(max_length=20,null=True,default=False)
    vehicle_class = models.CharField(max_length=20,null=True,default=False)
    issue_date = models.DateField(default=False)
    licence_validity = models.DateField(default=False)
    dob = models.DateField(auto_now_add=True,null=True,blank=False)

