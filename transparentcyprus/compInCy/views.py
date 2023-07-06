from django.shortcuts import render

# Create your views here.
def default(response):
    return render(response,'compincy/default.html')