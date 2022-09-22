from django.db import models
import uuid 
import all_details.models as all_details_models


# Create your models here.
class Website(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch = models.ForeignKey(all_details_models.Branch, on_delete=models.CASCADE,verbose_name='Branch')
    name = models.CharField(max_length=10000,  blank=True, null=True)
    ref_no = models.CharField(max_length=10000,  blank=True, null=True)
    address = models.CharField(max_length=10000, blank=True, null=True)
    locality = models.CharField(max_length=10000, blank=True, null=True)
    city = models.CharField(max_length=10000, blank=True, null=True)
    state = models.CharField(max_length=10000, blank=True, null=True)
    postalcode = models.CharField(max_length=10000, blank=True, null=True)
    country = models.CharField(max_length=10000, blank=True, null=True)
    mobileno = models.CharField(max_length=10000,blank=True, null=True,unique=True)
    refrenced_by = models.CharField(max_length=10000, blank=True, null=True)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    dateofbirth = models.DateField(null=True, blank=True)
    maritialstatus = models.CharField(max_length=100, null=True, blank=True)
    medication = models.CharField(max_length=100, null=True, blank=True)
    allergies = models.CharField(max_length=100, null=True, blank=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    emergency_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_no = models.CharField(max_length=100, null=True, blank=True)
    emergency_relationship = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return '%s' % str(self.id)

    class Meta:
            
            verbose_name = 'Website'