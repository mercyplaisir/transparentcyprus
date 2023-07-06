from django.shortcuts import render

# Create your views here.
def default(response):
    return render(response,"tourism/default.html")