from django.contrib import admin
from all_details import models

# Register your models here.
@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id','name') 

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','name','branch') 