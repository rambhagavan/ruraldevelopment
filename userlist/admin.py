from django.contrib import admin
from django.contrib.admin.sites import site
from userlist.models import supplier,company
# Register your models here.

class supplier_admin(admin.ModelAdmin):
    list_display=('id','name','city','state','zipcode')

class company_admin(admin.ModelAdmin):
    list_display=('id','name','city','state','zipcode')    
admin.site.register(supplier,supplier_admin)
admin.site.register(company,company_admin)

