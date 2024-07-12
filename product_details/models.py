from django.db import models
from django.forms import FileField
from userlist.models import supplier
from django.contrib.auth.models import User
# Create your models here.
class categorie(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class product(models.Model):
    category= models.ForeignKey(categorie, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    supplied_by=models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True)
    image=models.FileField(upload_to="product/", max_length=250,null=True,default=None)
    def __str__(self):
        return self.name