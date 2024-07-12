from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('J&K','J&K'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh	','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
)

class supplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=255, null = True)
    phone=models.CharField(max_length=50,null=True)
    profileimage=models.FileField(upload_to="profileimage/",max_length=100,null=True,default=None)
    city=models.CharField(max_length=50,null=True,blank=True, default="indore")
    state = models.CharField(choices=STATE_CHOICES,max_length=255,default="Madhya Pradesh")
    zipcode=models.CharField(max_length=50,null=True,blank=True, default=00000)
    def __str__(self):
        return self.user.username
    # though to add but created third table # hired_by=models.ForeignKey(company,on_delete=models.CASCADE)
    # though to add but created third table # product_supplied_to=models.ForeignKey(company,on_delete=models.CASCADE)
   
class company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=255,null = True)
    phone=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES,max_length=255)
    zipcode=models.CharField(max_length=50)
    # though to add but created third table  # hired_user=models.ForeignKey(supplier,on_delete=models.CASCADE)
    # though to add but created third table  # product=models.ForeignKey(supplier,on_delete=models.CASCADE)
    profileimage=models.FileField(upload_to="profileimage/",max_length=100,null=True,default=None)
    def __str__(self):
        return self.user.username
