from django.shortcuts import render
from . import models
# Create your views here.
def default(response):
    return render(response,"tourism/default.html")

def arrivals_at_airports_by_month(response):
    obj = models.Arrivals_at_airports_by_month.objects.all()
    return render(response,"tourism/arrivals_at_airports_by_month.html",{"objects":obj})
def tourism_revenue_23(response):
    obj = models.Tourism_revenue_23.objects.all()
    return render(response,"tourism/tourism_revenue_23.html",{"objects":obj})
def tourist_arrivals_per_month(response):
    obj = models.Tourist_arrivals_per_month.objects.all()
    return render(response,"tourism/tourist_arrivals_per_month.html",{"objects":obj})