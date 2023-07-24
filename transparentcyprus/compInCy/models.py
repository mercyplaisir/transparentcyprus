from django.db import models
from main.models import Categories
# Create your models here.
class ListOfOrg(models.Model):
    organisation_name = models.CharField(max_length=59)
    registration_no = models.CharField(max_length=50)
    organisation_type_code = models.CharField(max_length=50)
    organisation_type = models.CharField(max_length=50)
    organisation_sub_type = models.CharField(max_length=50)
    name_status_code = models.CharField(max_length=50)
    name_status = models.CharField(max_length=50)
    registration_date = models.CharField(max_length=50)
    organisation_status = models.CharField(max_length=50)
    organisation_status_date = models.CharField(max_length=50)
    address_seq_no = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)