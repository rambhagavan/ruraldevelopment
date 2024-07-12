from django.db import models
from userlist.models import supplier,company
from product_details.models import product

class relationtable(models.Model):
    suppliedby = models.ForeignKey(supplier,on_delete=models.CASCADE)
    productsupplied = models.ForeignKey(product,on_delete=models.CASCADE)
    suppliedto = models.ForeignKey(company,on_delete=models.CASCADE)
    Approval = models.CharField(max_length=50,default='N',null=True)