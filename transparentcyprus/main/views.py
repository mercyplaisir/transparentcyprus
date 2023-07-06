from django.shortcuts import render


# Create your views here.
def index(response):
    user = response.user
    return render(response,"main/base.html" ,{'user':user})

def homepage(response):
    
    return render(response,"main/home.html")
