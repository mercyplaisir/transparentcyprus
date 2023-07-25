from django.shortcuts import render

# Create your views here.
def default(response):
    return render(response,"realestate/default.html")

def real_estate_mortgage_statistics(response):
    return render(response,'realestate/real_estate_mortgage_statistics.html')
def real_estate_sales_to_foreigners(response):
    return render(response,'realestate/real_estate_sales_to_foreigners.html')
def sales_transfers_of_real_estate(response):
    return render(response,'realestate/sales_transfers_of_real_estate.html')
def statistics_of_real_estate_sales_documents(response):
    return render(response,'realestate/statistics_of_real_estate_sales_documents.html')
