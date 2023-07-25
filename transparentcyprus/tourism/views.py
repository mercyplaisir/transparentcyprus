from django.shortcuts import render

# Create your views here.
def default(response):
    return render(response,"tourism/default.html")

def arrivals_at_airports_by_month(response):
    return render(response,"tourism/arrivals_at_airports_by_month.html")
def tourism_revenue_23(response):
    return render(response,"tourism/tourism_revenue_23.html")
def tourist_arrivals_per_month(response):
    return render(response,"tourism/tourist_arrivals_per_month.html")