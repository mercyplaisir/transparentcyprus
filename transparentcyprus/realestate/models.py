from django.db import models
from main.models import Categories
# Create your models here.
class Real_estate_mortgage_statistics(models.Model):
    month = models.CharField(max_length=15)
    district = models.CharField(max_length=15)
    mortgages = models.CharField(max_length=15)
    total_amount = models.CharField(max_length=15)
    categorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)

class Real_estate_sales_to_foreigners(models.Model):
    month = models.CharField(max_length=15)
    description = models.CharField(max_length=70)
    category = models.CharField(max_length=15)
    nicosia = models.CharField(max_length=15)
    famagusta  = models.CharField(max_length=15)
    larnaca = models.CharField(max_length=15)
    limassol = models.CharField(max_length=15)
    pafos = models.CharField(max_length=15)
    all_districts = models.CharField(max_length=15)
    categorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
    
class Sales_transfers_of_real_estate(models.Model):
    month = models.CharField(max_length=15)
    district = models.CharField(max_length=15)
    cases = models.CharField(max_length=15)
    temaxia = models.CharField(max_length=15)
    total_declared_amount = models.CharField(max_length=30)
    total_accepted_amount = models.CharField(max_length=30)
    categorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)

class Statistics_of_real_estate_sales_documents(models.Model):
    month = models.CharField(max_length=15)
    nicosia = models.CharField(max_length=15)
    famagusta  = models.CharField(max_length=15)
    larnaca = models.CharField(max_length=15)
    limassol = models.CharField(max_length=15)
    pafos = models.CharField(max_length=15)
    categorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)