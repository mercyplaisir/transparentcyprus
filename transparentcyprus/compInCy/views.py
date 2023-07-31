from django.shortcuts import render
from . import models
# Create your views here.
def default(response):
    return render(response,'compincy/default.html')

def listOfOrg(response):
    obj = models.ListOfOrg.objects.all()
    return render(response,'compincy/listOfOrg.html',{"objects":obj})