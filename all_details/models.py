from django.db import models
import uuid 
# Create your models here. 

class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10000,  blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
            verbose_name = 'Branch'

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10000,  blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,verbose_name='Branch')
    def __str__(self):
        return self.name

    class Meta:
            verbose_name = 'Employee'