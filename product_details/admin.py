from django.contrib import admin
from .models import categorie,product
# Register your models here.

class category_admin(admin.ModelAdmin):
    list_display=('id','name',)
admin.site.register(categorie,category_admin)

class product_admin(admin.ModelAdmin):
    list_display=('id','name','image','description','supplied_by')
admin.site.register(product,product_admin)