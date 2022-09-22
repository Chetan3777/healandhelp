from weakref import WeakKeyDictionary
from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Website)
class BranchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Website._meta.get_fields()] 