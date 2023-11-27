from django.db import models

from main.models import Categories
# Create your models here.


# class Arrivals_at_airports_by_month(models.Model):
#     month = models.CharField(max_length=20)
#     larnaca_airport  = models.CharField(max_length=20)
#     paphos_airport = models.CharField(max_length=20) 
#     total_arrivals  = models.CharField(max_length=20)
#     categorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
# class Tourism_revenue_23(models.Model):
#     month = models.CharField(max_length=30)
#     revenue_in_million_euros = models.CharField(max_length=30)
#     revenue_per_capita_in_euros = models.CharField(max_length=30)
#     categorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
# class Tourist_arrivals_per_month(models.Model):
#     month = models.CharField(max_length=15)
#     arrivals = models.CharField(max_length=30)
#     categorie = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)