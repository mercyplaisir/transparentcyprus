from django.shortcuts import render
from . import models
# Create your views here.
def default(response):
    return render(response,"realestate/default.html")

def real_estate_mortgage_statistics(response):
    obj = models.Real_estate_mortgage_statistics.objects.all()
    return render(response,'realestate/real_estate_mortgage_statistics.html',{'objects':obj})

def real_estate_sales_to_foreigners(response):
    obj = models.Real_estate_sales_to_foreigners.objects.all()
    return render(response,'realestate/real_estate_sales_to_foreigners.html',{'objects':obj})

def sales_transfers_of_real_estate(response):
    obj = models.Sales_transfers_of_real_estate.objects.all()
    return render(response,'realestate/sales_transfers_of_real_estate.html',{'objects':obj})

def statistics_of_real_estate_sales_documents(response):
    obj = models.Statistics_of_real_estate_sales_documents.objects.all()
    return render(response,'realestate/statistics_of_real_estate_sales_documents.html',{'objects':obj})
