from django.contrib import admin
from .models import relationtable

class relation_admin(admin.ModelAdmin):
    list_display=('suppliedby','productsupplied','suppliedto','Approval')
admin.site.register(relationtable,relation_admin)